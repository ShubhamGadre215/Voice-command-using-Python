import re
from unittest import result
from pip import main
import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio 
import wikipedia
import webbrowser
import os

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice',voices[0].id)




def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    hour=int(datetime.datetime.now().hour)
    if(hour>=0 and hour<12):
        speak("Good morning Sir")

    elif(hour>=12 and hour<18):
        speak("Good afternoon Sir")

    else:
        speak("Good evening")


    speak("Hello  i am david, Plz tell me how may i help you sir...")


def takecommand():
    #it takes microphone input form user and gives string output to user
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning to you sir....")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing the Command plz wait...")
        query=r.recognize_google(audio,language='en-in')
        print(f"User Said: {query}")

    except Exception as e:
        print(f"{e}")

        print("Plz say that again...")
        return "None"
    
    return query

def sendEmail():
    pass
if __name__=="__main__":
   
    greetMe()
    if 1:
        query=takecommand().lower()
       #Logic for executing task based on query
        if("wikipedia" in query):
            speak('Searching in wikipedia')
            query=query.replace('wikipedia',"")
            result=wikipedia.summary(query,sentences=5)
            speak('According to wikipedia')
            print(result)
            speak(result)
        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open google" in query:
            webbrowser.open("google.com")

        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")

        elif "play music" in query:
            music_directory='This PC\\Music'
            songs=os.listdir(music_directory)
            print(songs)
            os.startfile(os.path.join(music_directory,songs[0]))


        elif "the time" in query:
            strtime=datetime.datetime.now().strftime("%H:%M:%S")
            print(strtime)
            speak(f" Sir The time is{strtime}")    
            
        elif "open vs code" in query:
            speak("Opening vs code")
            codepath="C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"   
            os.startfile(codepath) 

        elif "email to shubham"in query:
            try:
                speak("What mail should i send sir...")
                content=takecommand()
                to="shubhamgadre215@gmail.com"
                sendEmail(to,content)
                speak("Email has been send sir")

            except Exception as e:
                print(f"Sorry faild to send email due to this reason below \n {e}")    



    


