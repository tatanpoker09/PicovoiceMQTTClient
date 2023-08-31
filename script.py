import time

import pvrhino as pvrhino
from dotenv import load_dotenv

from texttospeech import speak
import paho.mqtt.client as mqtt

import os

from datetime import datetime
from threading import Thread
import pvporcupine
from pvrecorder import PvRecorder
import wakeonlan

load_dotenv()


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
        speak(intent + status, "Changing server status to %s" % status)
        change_server_status(status)
    elif intent == "turn_server_on":
        speak("change_server_statuson", "Changing server status to on")
        change_server_status("on")
    elif intent == "turn_server_off":
        speak("change_server_statusoff", "Changing server status to off")
        change_server_status("off")
    elif intent == "change_light_status":
        status = slots["light"]
        speak(intent + status, "Changing light status to %s" % status)
    elif intent == "ask_weather":
        speak(intent, "Weather is sunny")
    elif intent == "ask_time":
        speak(intent, "Current time is %s" % str(datetime.now()), cache=False)


class PorcupineClient(Thread):

    def __init__(
            self,
            access_key,
            sensitivities,
            rhino_client,
            keywords=None,
            sleep_delta=0.5):

        super(PorcupineClient, self).__init__()
        self._access_key = "SECRET"
        self.recorder = None
        self.keywords = keywords
        self.sleep_delta = sleep_delta
        self.rhino_client = rhino_client
        self.sensitivities = sensitivities

        self.porcupine = pvporcupine.create(
            access_key=access_key,
            keywords=keywords,
            sensitivities=sensitivities)

    def create_recoder(self, device_index):
        self.recorder = PvRecorder(device_index=device_index, frame_length=self.porcupine.frame_length)

        print(f'Created Recorder. Using device: {self.recorder.selected_device}')
        print('Listening {')
        for keyword, sensitivity in zip(self.keywords, self.sensitivities):
            print('  %s (%.2f)' % (keyword, sensitivity))
        print('}')

    def run(self):
        """
         Creates an input audio stream, instantiates an instance of Porcupine object, and monitors the audio stream for
         occurrences of the wake word(s). It prints the time of detection for each occurrence and the wake word.
         """
        try:
            sleep_delta = 0
            while True:
                pcm = self.recorder.read()

                result = self.porcupine.process(pcm)
                if sleep_delta == 0:
                    if result >= 0:
                        self.rhino_client.on_wake_word_detected(self.keywords[result])
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
            if self.porcupine is not None:
                self.porcupine.delete()

            if self.recorder is not None:
                self.recorder.delete()

    @classmethod
    def show_audio_devices(cls):
        devices = PvRecorder.get_available_devices()

        for i in range(len(devices)):
            print(f'index: {i}, device name: {devices[i]}')

    def start_recorder(self):
        self.recorder.start()


class RhinoClient():
    def __init__(self, recorder):
        self.recorder = recorder

    def on_wake_word_detected(self, wakeword):
        print('[%s] Detected %s' % (str(datetime.now()), wakeword))
        try:
            while True:
                pcm = self.recorder.read()
                is_finalized = self.rhino.process(pcm)
                if is_finalized:
                    inference = self.rhino.get_inference()
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
            self.recorder.stop()


def get_microphone_index_by_name(microphone_name, devices):
    index = 0
    if microphone_name is not None:
        index = None
        for i in range(len(devices)):
            if microphone_name in devices[i]:
                index = i
                break
        if index is None:
            raise ValueError("Couldn't find audio device with name '%s'" % microphone_name)
    return index


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("$SYS/#")


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))


def main():
    PorcupineClient.show_audio_devices()

    devices = PvRecorder.get_available_devices()
    microphone_name = os.getenv('PV_MICROPHONE')

    index = get_microphone_index_by_name(microphone_name, devices)
    print(f'Using device: {devices[index]}')

    access_key = os.getenv('PICOVOICE_ACCESS_KEY')

    MODEL_NAME = os.getenv('RHINO_MODEL_NAME')

    rhino = pvrhino.create(
        access_key=access_key,
        context_path=f'./models/{MODEL_NAME}'
    )

    porcupine_client = PorcupineClient(
        access_key=access_key,
        sensitivities=[0.5],
        keywords=['jarvis'],
        rhino_client=rhino
    )

    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect("mqtt.eclipseprojects.io", 1883, 60)
    porcupine_client.start_recorder()


if __name__ == '__main__':
    main()
