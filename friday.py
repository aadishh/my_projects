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
    master =  'master'
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("good morning" + master)
    elif hour >= 12 and hour < 18:
        speak("good afternoon" + master)
    else:
        speak("good evening" + master)

    speak("hello I am Friday , how can I help u ")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listning...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognising....")
        speak("Recognising...")
        query = r.recognize_google(audio, language="en-in")
        print(f"user said: (query)\n")

    except Exception:
        speak("say it again please.......")
        return"none"
        return query


if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand().lower()
        if 'wikipedia' in query:
            speak("searching.......")
            query = query.replace('wikipedia', "")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif'open gmail' in query:
            webbrowser.open("gmail.com")
        elif 'play music' in query:
            music_dir = 'D:\\music'
            n = random2.randint(0, 190)
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[n]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H,%M,%S")
            speak(f"sir , the time is (strTime)")
