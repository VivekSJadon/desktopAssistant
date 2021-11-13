import datetime
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    '''it wishes the user'''

    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")
    
    speak("How may I help you?")

def takeCommand():
    '''it takes your voice input and converts it in string output'''

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="eng-in")
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please..")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()

    query = takeCommand().lower()

    # how this assistant works follows on below if else statements

    if "wikipedia" in query:
        speak("Searching Wikipedia...")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)

    elif "open google" in query:
        webbrowser.open("google.com")
    
    elif "open youtube" in query:
        webbrowser.open("youtube.com")
    
    elif "open stackoverflow" in query:
        webbrowser.open("stackoverflow.com")

    elif "play songs" in query:
        song_dir = "D:\\Music\\Bollywood Songs"
        songs = os.listdir(song_dir)
        os.startfile(os.path.join(song_dir, songs[random.randint(0, len(songs)-1)]))

    elif "time" in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        print(strTime)
        speak(f"The time is {strTime}")

    elif "today's date" in query:
        strDate = datetime.datetime.now().strftime("%d/%m/%y")
        print(strDate)
        speak(f"Todays date is {strDate}")

    elif "open code" in query:
        codePath = "C:\\Users\\user\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codePath)
    
    elif "what is the meaning of" in query:
        try:
            speak("what do you want to search sir")
            word = takeCommand()
            webbrowser.open(f"google.com/search?q{word}") 
        except Exception as e:
            speak("Sorry, unable to understand it")








    
