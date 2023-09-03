import uuid
from datetime import datetime

from texttospeech import speak
import pvrhino as pvrhino
from pvrecorder import PvRecorder


class RhinoClient:
    def __init__(self, mqtt_client, ACCESS_KEY, RHINO_MODEL_NAME):
        self.rhino: pvrhino = pvrhino.create(
            access_key=ACCESS_KEY,
            context_path=f'./models/{RHINO_MODEL_NAME}',
        )
        self.recorder = None,
        self.mqtt_client = mqtt_client

    def create_recoder(self, device_index):
        self.recorder = PvRecorder(device_index=device_index, frame_length=self.rhino.frame_length)
        print(f'Created Recorder. Using device: {self.recorder.selected_device}')

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
                        log_intent_recognition(inference)
                    else:
                        speak(None, "Didn't understand the command.")
                    break
        except KeyboardInterrupt:
            print('Stopping ...')
        finally:
            self.recorder.stop()

    def on_intent_recognized(self, intent, slots):
        topic = intent
        conversation_id = uuid.uuid1()
        payload = {
            "intent": intent,
            "slots": slots,
            "origin": "rhino",
            "conversation_id": str(conversation_id)
        }
        self.mqtt_client.publish(topic, payload)


def log_intent_recognition(inference):
    print('{')
    print("  intent : '%s'" % inference.intent)
    print('  slots : {')
    for slot, value in inference.slots.items():
        print("    %s : '%s'" % (slot, value))
    print('  }')
    print('}\n')
