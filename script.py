import time

import pvrhino as pvrhino
from dotenv import load_dotenv

load_dotenv()
import os

from datetime import datetime
from threading import Thread

import pvporcupine
from pvrecorder import PvRecorder
import wakeonlan

MODELS_PATH = "porcupine_models" + os.sep + "linux" + os.sep
KEYWORD_PATHS = [MODELS_PATH + "yo-journey.ppn", MODELS_PATH + "hey-journey.ppn"]
rhino = None
recorder = None


import time

import pvrhino as pvrhino
from dotenv import load_dotenv

load_dotenv()
import os

from datetime import datetime
from threading import Thread

import pvporcupine
from pvrecorder import PvRecorder
import wakeonlan

MODELS_PATH = "porcupine_models" + os.sep + "linux" + os.sep
KEYWORD_PATHS = [MODELS_PATH + "yo-journey.ppn", MODELS_PATH + "hey-journey.ppn"]
rhino = None
recorder = None


def change_server_status(status):
    if status == "on":
        wakeonlan.send_magic_packet(os.getenv("SERVER_MAC_ADDRESS"))
"script.py" 213L, 7156B                                                                                                                        1,1           Top

root@DietPi:~/.ssh# cd ..
root@DietPi:~# s
-bash: s: command not found
root@DietPi:~# ls
''$'\001\320\005''@8@8'$'\t''@!'$'\006\004''@@@'$'\370\001\370\001\b\003\004''8'$'\002''8'$'\002''8'$'\002\034\034\001\001\005'   PicovoiceMQTTClient   upsnap
Media																  immich-app
root@DietPi:~# cd PicovoiceMQTTClient/
root@DietPi:~/PicovoiceMQTTClient# python3 script.py
PorcupineClient.show_audio_devices()
devices = PvRecorder.get_available_devices()
index = 0  # MacBook Air Microphone
print(f'Using device: {devices[index]}')


access_key = os.getenv('PICOVOICE_ACCESS_KEY')


rhino = pvrhino.create(
    access_key=access_key,
    context_path='./models/SiliconRoom_en_raspberry-pi_v2_2_0.rhn'
)

PorcupineClient(
    access_key=access_key,
    library_path=None,
    model_path=None,
    keyword_paths=None,
    sensitivities=[0.5],
    output_path=None,
    keywords=['picovoice'],
    input_device_index=index).run()

"script.py" 213L, 7165B                                                                                                                        198,56        98%
context_path='./models/SiliconRoom_en_raspberry-pi_v2_2_0.rhn'
index: 0, device name: Discard all samples (playback) or generate zero samples (capture)
Using device: Discard all samples (playback) or generate zero samples (capture)


access_key = os.getenv('PICOVOICE_ACCESS_KEY')


rhino = pvrhino.create(
    access_key=access_key,
    context_path='./models/SiliconRoom_en_raspberry-pi_v2_2_0.rhn'
)

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
    # main()
    change_server_status('on')
"script.py" 214L, 7196B                                                                                                                        214,29        Bot
keywords=['picovoice'],
[ERROR] context file has incorrect format or belongs to a different platform
[ERROR] failed to load context with 'INVALID_ARGUMENT'
    Traceback (most recent call last):
File "/root/PicovoiceMQTTClient/script.py", line 213, in <module>
main()
File "/root/PicovoiceMQTTClient/script.py", line 196, in main
rhino = pvrhino.create(
    File "/usr/local/lib/python3.9/dist-packages/pvrhino/_factory.py", line 55, in create
return Rhino(
    File "/usr/local/lib/python3.9/dist-packages/pvrhino/_rhino.py", line 189, in __init__
PICOVOICE_ACCESS_KEY=OCINvPkTfEd5nZtoTLjN1eT8mOH/DoMr12uaCu/r9qDm6EuREAkHrg==
                     SERVER_MAC_ADDRESS=74:56:3c:6f:79:11
SERVER_IP_ADDRESS=192.168.50.104
SSH_KEY_PATH=/home/pi/.ssh/id_rsa
SSH_USER=tatan
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
".env" 5L, 197B                                                                                                                                5,14          All
raise self._PICOVOICE_STATUS_TO_EXCEPTION[status]()
pvrhino._rhino.RhinoInvalidArgumentError
root@DietPi:~/PicovoiceMQTTClient# vim script.py
root@DietPi:~/PicovoiceMQTTClient# python3 script.py
index: 0, device name: Discard all samples (playback) or generate zero samples (capture)
PICOVOICE_ACCESS_KEY=OCINvPkTfEd5nZtoTLjN1eT8mOH/DoMr12uaCu/r9qDm6EuREAkHrg==
SERVER_MAC_ADDRESS=74:56:3c:6f:79:11
SERVER_IP_ADDRESS=192.168.50.104
SSH_KEY_PATH=/home/pi/.ssh/id_rsa
SSH_USER=tatan
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
".env" 5L, 197B                                                                                                                                5,14          All
Using device: Discard all samples (playback) or generate zero samples (capture)
Using device: Discard all samples (playback) or generate zero samples (capture)
Listening {
    picovoice (0.50)
}
^CStopping ...
root@DietPi:~/PicovoiceMQTTClient# vim script.py
root@DietPi:~/PicovoiceMQTTClient# python3 script.py
root@DietPi:~/PicovoiceMQTTClient# vim script.py
root@DietPi:~/PicovoiceMQTTClient# python3 script.py
Warning: Identity file $/home/pi/.ssh/id_rsa not accessible: No such file or directory.
usage: ssh [-46AaCfGgKkMNnqsTtVvXxYy] [-B bind_interface]
[-b bind_address] [-c cipher_spec] [-D [bind_address:]port]
[-E log_file] [-e escape_char] [-F configfile] [-I pkcs11]
[-i identity_file] [-J [user@]host[:port]] [-L address]
PICOVOICE_ACCESS_KEY=OCINvPkTfEd5nZtoTLjN1eT8mOH/DoMr12uaCu/r9qDm6EuREAkHrg==
SERVER_MAC_ADDRESS=74:56:3c:6f:79:11
SERVER_IP_ADDRESS=192.168.50.104
SSH_KEY_PATH=/home/pi/.ssh/id_rsa
SSH_USER=tatan
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
".env" 5L, 197B                                                                                                                                5,14          All
PICOVOICE_ACCESS_KEY=OCINvPkTfEd5nZtoTLjN1eT8mOH/DoMr12uaCu/r9qDm6EuREAkHrg==
[-l login_name] [-m mac_spec] [-O ctl_cmd] [-o option] [-p port]
[-Q query_option] [-R address] [-S ctl_path] [-W host:port]
[-w local_tun[:remote_tun]] destination [command]
root@DietPi:~/PicovoiceMQTTClient# vim .env
root@DietPi:~/PicovoiceMQTTClient# ls
README.md  models  requirements.txt  script.py
root@DietPi:~/PicovoiceMQTTClient# pwd
/root/PicovoiceMQTTClient
root@DietPi:~/PicovoiceMQTTClient# vim .env
root@DietPi:~/PicovoiceMQTTClient# cd


access_key = os.getenv('PICOVOICE_ACCESS_KEY')


rhino = pvrhino.create(
    access_key=access_key,
    context_path='./models/SiliconRoom_en_raspberry-pi_v2_2_0.rhn'
)

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
    # main()
    change_server_status('off')
"script.py" 214L, 7197B                                                                                                                        214,28        Bot
print(f"If all other arguments seem valid, ensure that '{self._access_key}' is a valid AccessKey")
root@DietPi:~# ls
''$'\001\320\005''@8@8'$'\t''@!'$'\006\004''@@@'$'\370\001\370\001\b\003\004''8'$'\002''8'$'\002''8'$'\002\034\034\001\001\005'   PicovoiceMQTTClient   upsnap
Media																  immich-app
root@DietPi:~# pwd
/root
root@DietPi:~# cd .ssh
root@DietPi:~/.ssh# ls
id_rsa	id_rsa.pub  known_hosts
root@DietPi:~/.ssh# cd ..
root@DietPi:~# ls
''$'\001\320\005''@8@8'$'\t''@!'$'\006\004''@@@'$'\370\001\370\001\b\003\004''8'$'\002''8'$'\002''8'$'\002\034\034\001\001\005'   PicovoiceMQTTClient   upsnap
Media																  immich-app
root@DietPi:~# cd PicovoiceMQTTClient/
root@DietPi:~/PicovoiceMQTTClient# vim .env
root@DietPi:~/PicovoiceMQTTClient# python3 script.py
Warning: Identity file $/root/.ssh/id_rsa not accessible: No such file or directory.
usage: ssh [-46AaCfGgKkMNnqsTtVvXxYy] [-B bind_interface]
[-b bind_address] [-c cipher_spec] [-D [bind_address:]port]
[-E log_file] [-e escape_char] [-F configfile] [-I pkcs11]
[-i identity_file] [-J [user@]host[:port]] [-L address]
[-l login_name] [-m mac_spec] [-O ctl_cmd] [-o option] [-p port]
[-Q query_option] [-R address] [-S ctl_path] [-W host:port]
[-w local_tun[:remote_tun]] destination [command]
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
"script.py" 214L, 7194B                                                                                                                        166,33        81%
root@DietPi:~/PicovoiceMQTTClient# vim script.py
PICOVOICE_ACCESS_KEY=OCINvPkTfEd5nZtoTLjN1eT8mOH/DoMr12uaCu/r9qDm6EuREAkHrg==
SERVER_MAC_ADDRESS=74:56:3c:6f:79:11
SERVER_IP_ADDRESS=192.168.50.104
SSH_KEY_PATH=/root/.ssh/id_rsa
SSH_USER=tatan
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
".env" 5L, 194B                                                                                                                                4,18          All
PICOVOICE_ACCESS_KEY=OCINvPkTfEd5nZtoTLjN1eT8mOH/DoMr12uaCu/r9qDm6EuREAkHrg==
root@DietPi:~/PicovoiceMQTTClient# python3 script.py
None@192.168.50.104: Permission denied (publickey).
root@DietPi:~/PicovoiceMQTTClient# ls
PICOVOICE_ACCESS_KEY=OCINvPkTfEd5nZtoTLjN1eT8mOH/DoMr12uaCu/r9qDm6EuREAkHrg==
SERVER_MAC_ADDRESS=74:56:3c:6f:79:11
SERVER_IP_ADDRESS=192.168.50.104
SSH_KEY_PATH=./siliconserver
SSH_USER=tatan
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
".env" 5L, 192B                                                                                                                                4,28          All
PICOVOICE_ACCESS_KEY=OCINvPkTfEd5nZtoTLjN1eT8mOH/DoMr12uaCu/r9qDm6EuREAkHrg==
README.md  models  requirements.txt  script.py
import pvrhino as pvrhino
from dotenv import load_dotenv

load_dotenv()
import os

from datetime import datetime
from threading import Thread

import pvporcupine
from pvrecorder import PvRecorder
import wakeonlan

MODELS_PATH = "porcupine_models" + os.sep + "linux" + os.sep
KEYWORD_PATHS = [MODELS_PATH + "yo-journey.ppn", MODELS_PATH + "hey-journey.ppn"]
rhino = None
recorder = None


def change_server_status(status):
    if status == "on":
        wakeonlan.send_magic_packet(os.getenv("SERVER_MAC_ADDRESS"))
    elif status == "off":
        ssh_key_path = os.getenv("SSH_KEY_PATH")
"script.py" 214L, 7194B                                                                                                                        21,0-1         1%
def change_server_status(status):
    root@DietPi:~/PicovoiceMQTTClient# cd ..
PICOVOICE_ACCESS_KEY=OCINvPkTfEd5nZtoTLjN1eT8mOH/DoMr12uaCu/r9qDm6EuREAkHrg==
SERVER_MAC_ADDRESS=74:56:3c:6f:79:11
SERVER_IP_ADDRESS=192.168.50.104
SSH_KEY_PATH=./siliconserver
SSH_USER=tatan
~
~
~
~
~
~
~
~
~
~
import time

import pvrhino as pvrhino
from dotenv import load_dotenv

load_dotenv()
import os

from datetime import datetime
from threading import Thread

import pvporcupine
from pvrecorder import PvRecorder
import wakeonlan

MODELS_PATH = "porcupine_models" + os.sep + "linux" + os.sep
KEYWORD_PATHS = [MODELS_PATH + "yo-journey.ppn", MODELS_PATH + "hey-journey.ppn"]
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
        print("Changing server status to %s" % status)
        change_server_status(status)
"script.py" 214L, 7187B                                                                                                                               27,45         Top
import time

import pvrhino as pvrhino
from dotenv import load_dotenv

load_dotenv()
import os

from datetime import datetime
from threading import Thread

import pvporcupine
from pvrecorder import PvRecorder
import wakeonlan

MODELS_PATH = "porcupine_models" + os.sep + "linux" + os.sep
KEYWORD_PATHS = [MODELS_PATH + "yo-journey.ppn", MODELS_PATH + "hey-journey.ppn"]
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
        print("Changing server status to %s" % status)
        change_server_status(status)
    elif intent == "turn_server_on":
        print("Turning server on")
        change_server_status("on")
    elif intent == "turn_server_off":
        print("Turning server off")
        change_server_status("off")
    elif intent == "change_light_status":
        status = slots["light"]
        print("Changing light status to %s" % status)
    elif intent == "ask_weather":
        print("Weather is sunny")
    elif intent == "ask_time":
        print("Current time is %s" % str(datetime.now()))

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
                    print("Didn't understand the command.\n")
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


    rhino = pvrhino.create(
        access_key=access_key,
        context_path='./models/SiliconRoom_en_mac_v2_2_0.rhn'
    )

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
