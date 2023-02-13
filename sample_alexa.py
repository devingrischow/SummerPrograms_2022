import pyaudio


import speech_recognition as sr

r1 = sr.Recognizer()

with sr.Microphone() as source:
    print("listenined")

    audio = (r1.recognize_sphinx(audio))