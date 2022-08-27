import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import os
import smtplib
import webbrowser
import random2

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    name = 'Rishab'
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("good morning" + name)
    elif hour >= 12 and hour < 18:
        speak("good afternoon" + name)
    else:
        speak("good evening" + name)

    speak("hello I am Friday , how can I help u ")

if __name__ == "__main__":
    wishme()
