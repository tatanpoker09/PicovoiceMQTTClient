from gtts import gTTS
import os


def speak(self, intent, text, language="en"):
    if not os.path.exists(f"./audio/{intent}.mp3"):
        tts = gTTS(text=text, lang=language, slow=False)
        tts.save(f"./audio/{intent}.mp3")
    os.system(f"mpg123 ./audio/{intent}.mp3")
