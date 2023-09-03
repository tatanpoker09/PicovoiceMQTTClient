import os
import time
from threading import Thread

import pvporcupine
from dotenv import load_dotenv
import pvrhino

from common.mqtt import MqttClient
from rhino_client import RhinoClient
from pvrecorder import PvRecorder

load_dotenv()


# if intent == "change_server_status":
#     status = slots["server"]
#     speak(intent + status, "Changing server status to %s" % status)
#     change_server_status(status)
# elif intent == "turn_server_on":
#     speak("change_server_statuson", "Changing server status to on")
#     change_server_status("on")
# elif intent == "turn_server_off":
#     speak("change_server_statusoff", "Changing server status to off")
#     change_server_status("off")
# elif intent == "change_light_status":
#     status = slots["light"]
#     speak(intent + status, "Changing light status to %s" % status)
# elif intent == "ask_weather":
#     speak(intent, "Weather is sunny")
# elif intent == "ask_time":
#     speak(intent, "Current time is %s" % str(datetime.now()), cache=False)


class PorcupineClient(Thread):
    def __init__(
            self,
            access_key: str,
            sensitivities: list,
            rhino_client: pvrhino,
            recorder: PvRecorder,
            keywords=None,
            sleep_delta=0.5):

        super(PorcupineClient, self).__init__()
        self._access_key = "SECRET"
        self.recorder = recorder,
        self.keywords = keywords
        self.sleep_delta = sleep_delta
        self.rhino_client = rhino_client
        self.sensitivities = sensitivities

        self.porcupine = pvporcupine.create(
            access_key=access_key,
            keywords=keywords,
            sensitivities=sensitivities)

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


def main():
    PorcupineClient.show_audio_devices()

    devices = PvRecorder.get_available_devices()
    microphone_name = os.getenv('PV_MICROPHONE')

    index = get_microphone_index_by_name(microphone_name, devices)
    print(f'Using device: {devices[index]}')

    ACCESS_KEY = os.getenv('PICOVOICE_ACCESS_KEY')

    RHINO_MODEL_NAME = os.getenv('RHINO_MODEL_NAME')

    mqtt_broker_address, mqtt_broker_port = os.getenv('MQTT_BROKER_ADDRESS'), os.getenv('MQTT_BROKER_PORT')
    mqtt_client = MqttClient(mqtt_broker_address, mqtt_broker_port)
    rhino_client = RhinoClient(mqtt_client, ACCESS_KEY, RHINO_MODEL_NAME)
    rhino_client.create_recoder(index)

    porcupine_client = PorcupineClient(
        access_key=ACCESS_KEY,
        sensitivities=[0.5],
        keywords=['jarvis'],
        rhino_client=rhino_client.rhino,
        recorder=rhino_client.recorder,
    )

    porcupine_client.start_recorder()


if __name__ == '__main__':
    main()
