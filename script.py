import time

from dotenv import load_dotenv

load_dotenv()
import os
import struct
import wave
from datetime import datetime
from threading import Thread

import pvporcupine
from pvrecorder import PvRecorder

MODELS_PATH = "porcupine_models" + os.sep + "linux" + os.sep
KEYWORD_PATHS = [MODELS_PATH + "yo-journey.ppn", MODELS_PATH + "hey-journey.ppn"]


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

        super(PorcupineClient   , self).__init__()

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

        porcupine = None
        recorder = None
        wav_file = None
        try:
            porcupine = pvporcupine.create(
                access_key=self._access_key,
                keywords=self.keywords,
                sensitivities=self._sensitivities)

            recorder = PvRecorder(device_index=self._input_device_index, frame_length=porcupine.frame_length)
            recorder.start()

            if self._output_path is not None:
                wav_file = wave.open(self._output_path, "w")
                wav_file.setparams((1, 2, 16000, 512, "NONE", "NONE"))

            print(f'Using device: {recorder.selected_device}')

            print('Listening {')
            for keyword, sensitivity in zip(self.keywords, self._sensitivities):
                print('  %s (%.2f)' % (keyword, sensitivity))
            print('}')
            sleep_delta = 0
            while True:
                pcm = recorder.read()

                if wav_file is not None:
                    wav_file.writeframes(struct.pack("h" * len(pcm), *pcm))

                result = porcupine.process(pcm)
                if sleep_delta == 0:
                    if result >= 0:
                        print('[%s] Detected %s' % (str(datetime.now()), self.keywords[result]))
                        recorder.stop()
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
    PorcupineClient.show_audio_devices()
    devices = PvRecorder.get_available_devices()
    index = 0  # MacBook Air Microphone
    print(f'Using device: {devices[index]}')

    access_key = os.getenv('PICOVOICE_ACCESS_KEY')
    PorcupineClient(
        access_key=access_key,
        library_path=None,
        model_path=None,
        keyword_paths=None,
        sensitivities=[0.5],
        output_path=None,
        keywords=['picovoice'],
        input_device_index=index).run()


if __name__ == '__main__':
    main()
