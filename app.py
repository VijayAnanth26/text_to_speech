from gtts import gTTS

import os

mytext = input("Enter your text:")

language = 'en'

myobj = gTTS(text=mytext, lang=language, slow=False)

myobj.save("Audio.mp3")

os.system("start Audio.mp3")
