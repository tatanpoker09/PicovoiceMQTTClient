from gtts import gTTS
import os
mytext = 'Welcome to geeksforgeeks!'
language = 'en'
tts = gTTS(text=mytext, lang=language, slow=False)
tts.save("welcome.mp3")
# Playing the converted file
os.system("mpg123 welcome.mp3")