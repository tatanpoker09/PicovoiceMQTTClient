from gtts import gTTS
import os


def speak(cache_value, text, cache=True, language="en"):
    if not os.path.exists(f"./audio/{cache_value}.mp3") or not cache:
        tts = gTTS(text=text, lang=language, slow=False)
        tts.save(f"./audio/{cache_value}.mp3")
    os.system(f"mpg123 ./audio/{cache_value}.mp3")
