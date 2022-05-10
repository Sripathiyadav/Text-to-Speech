#pip install gtts
#pip install playsound
from gtts import gTTS
from playsound import playsound

audio = 'speech.mp3'
language = 'en'
sp = gTTS(text = "hello sripathi, im your computer ",lang=language,slow=False)
sp.save(audio)
playsound(audio)
