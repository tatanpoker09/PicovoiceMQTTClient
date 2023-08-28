import time

import pvrhino as pvrhino
from dotenv import load_dotenv

from texttospeech import speak

load_dotenv()

import os

from datetime import datetime
from threading import Thread

import pvporcupine
from pvrecorder import PvRecorder
import wakeonlan

rhino = None
recorder = None


def change_server_status(status):
    if status == "on":
        wakeonlan.send_magic_packet(os.getenv("SERVER_MAC_ADDRESS"))
    elif status == "off":
        ssh_key_path = os.getenv("SSH_KEY_PATH")
        server_username = os.getenv("SSH_USER")
        server_ip_address = os.getenv("SERVER_IP_ADDRESS")
        os.system(f"ssh -i {ssh_key_path} -o StrictHostKeyChecking=no {server_username}@{server_ip_address} "
                  f"'sudo -S poweroff'")


def on_intent_recognized(intent, slots):
    if intent == "change_server_status":
        status = slots["server"]
        speak(intent+status, "Changing server status to %s" % status)
        change_server_status(status)
    elif intent == "turn_server_on":
        speak("change_server_statuson", "Changing server status to on")
        change_server_status("on")
    elif intent == "turn_server_off":
        speak("change_server_statusoff", "Changing server status to off")
        change_server_status("off")
    elif intent == "change_light_status":
        status = slots["light"]
        speak(intent+status, "Changing light status to %s" % status)
    elif intent == "ask_weather":
        speak(intent, "Weather is sunny")
    elif intent == "ask_time":
        speak(intent, "Current time is %s" % str(datetime.now()), cache=False)



def on_wake_word_detected(wakeword):
    global rhino
    global recorder
    print('[%s] Detected %s' % (str(datetime.now()), wakeword))
    try:
        while True:
            pcm = recorder.read()
            is_finalized = rhino.process(pcm)
            if is_finalized:
                inference = rhino.get_inference()
                if inference.is_understood:
                    on_intent_recognized(inference.intent, inference.slots)
                    print('{')
                    print("  intent : '%s'" % inference.intent)
                    print('  slots : {')
                    for slot, value in inference.slots.items():
                        print("    %s : '%s'" % (slot, value))
                    print('  }')
                    print('}\n')
                else:
                    speak(None, "Didn't understand the command.")
                break
    except KeyboardInterrupt:
        print('Stopping ...')
    finally:
        recorder.stop()


class PorcupineClient(Thread):
    def __init__(
            self,
            access_key,
            library_path,
            model_path,
            keyword_paths,
            sensitivities,
            input_device_index=None,
            output_path=None,
            keywords=None,
            sleep_delta=0.5):

        super(PorcupineClient, self).__init__()

        self._access_key = access_key
        self._library_path = library_path
        self._model_path = model_path
        self._keyword_paths = keyword_paths
        self._sensitivities = sensitivities
        self._input_device_index = input_device_index
        self.sleep_delta = sleep_delta
        self._output_path = output_path
        self.keywords = keywords

    def run(self):
        """
         Creates an input audio stream, instantiates an instance of Porcupine object, and monitors the audio stream for
         occurrences of the wake word(s). It prints the time of detection for each occurrence and the wake word.
         """
        # for x in self._keyword_paths:
        #     keyword_phrase_part = os.path.basename(x).replace('.ppn', '').split('_')
        #     if len(keyword_phrase_part) > 6:
        #         keywords.append(' '.join(keyword_phrase_part[0:-6]))
        #     else:
        #         keywords.append(keyword_phrase_part[0])
        global recorder
        porcupine = None
        wav_file = None
        try:
            porcupine = pvporcupine.create(
                access_key=self._access_key,
                keywords=self.keywords,
                model_path=self._model_path,
                sensitivities=self._sensitivities)

            recorder = PvRecorder(device_index=self._input_device_index, frame_length=porcupine.frame_length)
            recorder.start()

            print(f'Using device: {recorder.selected_device}')
            print('Listening {')
            for keyword, sensitivity in zip(self.keywords, self._sensitivities):
                print('  %s (%.2f)' % (keyword, sensitivity))
            print('}')

            sleep_delta = 0
            while True:
                pcm = recorder.read()

                result = porcupine.process(pcm)
                if sleep_delta == 0:
                    if result >= 0:
                        on_wake_word_detected(self.keywords[result])
                        recorder.start()
                        sleep_delta = self.sleep_delta
                else:
                    sleep_delta = max(sleep_delta - time.time(), 0)

        except pvporcupine.PorcupineInvalidArgumentError as e:
            print(f"If all other arguments seem valid, ensure that '{self._access_key}' is a valid AccessKey")
            raise e
        except pvporcupine.PorcupineActivationError as e:
            print("AccessKey activation error")
            raise e
        except pvporcupine.PorcupineActivationLimitError as e:
            print(f"AccessKey '{self._access_key}' has reached it's temporary device limit")
            raise e
        except pvporcupine.PorcupineActivationRefusedError as e:
            print(f"AccessKey '{self._access_key}' refused")
            raise e
        except pvporcupine.PorcupineActivationThrottledError as e:
            print(f"AccessKey '{self._access_key}' has been throttled")
            raise e
        except pvporcupine.PorcupineError as e:
            print(f"Failed to initialize Porcupine")
            raise e
        except KeyboardInterrupt:
            print('Stopping ...')
        finally:
            if porcupine is not None:
                porcupine.delete()

            if recorder is not None:
                recorder.delete()

            if wav_file is not None:
                wav_file.close()

    @classmethod
    def show_audio_devices(cls):
        devices = PvRecorder.get_available_devices()

        for i in range(len(devices)):
            print(f'index: {i}, device name: {devices[i]}')


def main():
    global rhino
    PorcupineClient.show_audio_devices()
    devices = PvRecorder.get_available_devices()
    index = 0  # MacBook Air Microphone
    print(f'Using device: {devices[index]}')

    access_key = os.getenv('PICOVOICE_ACCESS_KEY')

    MODEL_NAME=os.getenv("MODEL_NAME")
    rhino = pvrhino.create(
        access_key=access_key,
        context_path=f'./models/{MODEL_NAME}'
    )

    PorcupineClient(
        access_key=access_key,
        library_path=None,
        model_path=None,
        keyword_paths='./models/Jarvis_en_raspberry-pi_v2_2_0.ppn',
        sensitivities=[0.5],
        output_path=None,
        keywords=['Jarvis'],
        input_device_index=index).run()


if __name__ == '__main__':
    main()
