import json
import os
import time
from time import ctime

import requests
import speech_recognition as sr
from gtts import gTTS


def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I am listening...")
        audio = r.listen(source)
    data = ""
    try:
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition did not understand audio")
    except sr.RequestError as e:
        print("Request Failed; {0}".format(e))
    return data


def respond(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='en')
    tts.save("speech.mp3")
    os.system("mpg321 speech.mp3")


def digital_assistant(data):
    if "how are you" in data:
        listening = True
        respond("I am well")

    if "what time is it" in data:
        listening = True
        respond(ctime())
        
    if "stop listening" in data:
        listening = False
        print('Listening stopped')
        return listening
    return listening

