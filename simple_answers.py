import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import os

mic = sr.Recognizer()
with sr.Microphone() as source:
    print("Pergunte algo!")
    audio = mic.listen(source)

fala = mic.recognize_google(audio, language="pt-BR")

if fala.lower() == "como você está":
    txt = gTTS(text="Eu estou bem, e você?", lang="pt-br")
elif fala.lower() == "qual o seu nome":
    txt = gTTS(text="Meu nome é Ana", lang="pt-br")
else:
    txt = gTTS(text="Desculpe! Não entendi.", lang="pt-br")

txt.save("./resp.mp3")
playsound("./resp.mp3")
os.remove("./resp.mp3")