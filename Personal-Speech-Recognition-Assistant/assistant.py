#pip install pyaudio
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr  #pip install speechRecognition
import wikipedia #pip install wikipedia
import webbrowser
import os
import datetime
import time
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning!!")

    elif hour>12 and hour<=15:
        speak("Good Afternoon!!")

    elif hour>=15 and hour<=18:
        speak("Good Evening!!")

    else:
        speak("Good Night")

    speak("I am Jarvis. Please tell me how may I help you!")


def takeCommand():
    # Taking input via microphone from the user and returns output as string
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 1000
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        speak(audio)

    try:
        print("Reconizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"Abhishek said : {query}\n")
        speak(f"Abhishek said : {query}\n")

    except Exception as e:
        speak("Say that again please...")
        return "None"
    return query

if __name__ == "__main__":
    wishme()
    #speak("Abhishek is my originator")
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query: # Eg. wikipedia "awards"
            speak('Searching wikipedia...')
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(result)
            speak(result)

        elif 'youtube' in query: # Eg. youtube "dhruv rathee"
            search = query.split(" ")[1]
            url = f"https://www.youtube.com/results?search_query={search}"
            webbrowser.get().open(url)

        elif 'google' in query: # Eg. google "WhatsApp"
            search = query.split(" ")[1]
            webbrowser.get().open(f"https://google.com/search?q={search}")

        elif 'facebook' in query:
            webbrowser.open("facebook.com")

        elif 'insta' in query:
            webbrowser.open("instagram.com")

        elif 'spotify' in query:
            webbrowser.open("https://open.spotify.com/collection/tracks")

        elif 'music' in query:
            music_dir = 'C:\\Users\\akdps\\Documents\\lets code\\Personal-Speech-Recognition-Assistant\\music'
            songs = os.listdir(music_dir)
            print(songs)
            speak(f"you have these songs {songs}")
        # To play the first song!
            #os.startfile(os.path.join(music_dir, songs[0]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, The Time is {strTime}")

        elif 'application' in query: # Run apps by giving the codepath of the application
            codepath = "C:\\Program Files\\RStudio\\bin\\rstudio.exe"
            os.startfile(codepath)

        elif 'how are you' in query:
            speak("fine sir! and what about you")

        elif 'good' in query:
            speak("great sir")

        elif 'favourite movie' in query:
            speak("Avatar: The Way of Water")

        elif 'who is the father' in query:
            speak("Abhishek")

        elif 'family member' in query:
            speak("there are 6 members in my family")

        elif 'president' in query:
            speak("President of INDIA is Droupadi Murmu")

        elif 'corona' in query:
            speak("Coronavirus disease (COVID-19) is an infectious disease caused by a newly discovered coronavirus. Most people who fall sick with COVID-19 will experience mild to moderate symptoms and recover without special treatment.")

        elif 'safe' in query:
            speak("Maintain at least 1 metre (3 feet) distance between yourself and others. And Regularly and thoroughly clean your hands with an alcohol-based hand rub or wash them with soap and water")

        elif 'who are you' in query:
            speak("I am robot")

        elif 'Krishna' in query:
            speak("he is my originator. and he is a great man and also a fun loving guys and i know his secret hahahaha... but i don't tell you")

        elif 'friend' in query:
            speak("abhishek have many friends like amit, rahul, hrithik, chintu, mintu")

        elif 'brother and sister' in query:
            speak("abhay raj, madhu kumari and laxmi kumari. These all are my brother and sisters")

        elif 'birthday' in query:
            x = datetime.datetime.now().strftime("%m-%d")
            if x == "03-05":
                speak("Happy Birthday sir!!")
            else:
                speak("Today is not you birthday")

        elif 'calculator' in query: # Run via terminal for user inputs
            speak("what you want like addition,subtraction,multiplication,division")

        elif 'addition' in query:
            speak("enter first number")
            x=int(input())
            speak("enter second number")
            y=int(input())
            add=x+y
            speak(add)

        elif 'subtraction' in query:
            speak("enter first number")
            x = int(input())
            speak("enter second number")
            y = int(input())
            sub=x-y
            speak(sub)

        elif 'multiplication' in query:
            speak("enter first number")
            x = int(input())
            speak("enter second number")
            y = int(input())
            mul=x-y
            speak(mul)

        elif 'division' in query:
            speak("enter first number")
            x = int(input())
            speak("enter second number")
            y = int(input())
            div=x/y
            speak(div)

        elif 'details' in query:
            f = open("details.txt")
            content = f.read()
            speak(content)
            f.close()

        elif 'shayari' in query:
            f = open("shayari.txt")
            content = f.read()
            speak(content)
            f.close()

        elif 'quotes' in query: #kotes
            f = open("quotes.txt")
            content = f.read()
            speak(content)
            f.close()

        elif 'poem' in query:
            f = open("poem.txt")
            content = f.read()
            speak(content)
            f.close()

        elif 'quit' in query:
            speak("Happy to serve you sir! goodbye! see you soon!")
            exit()