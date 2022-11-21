import datetime
from datetime import date
import os
import random
import webbrowser
import smtplib 
import pyttsx3
import speech_recognition as sr
import wikipedia

import requests, json

# from ast import main   


engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices') 
# print(voices[0].id)  
engine.setProperty('voice',voices[0].id) 





def speak(audio):
    engine.say(audio)
    engine.runAndWait()  

def wishMe():
    hour=int(datetime.datetime.now().hour)
    
    if hour>=0 and hour<12:
        speak("Good Morning sir !")
    elif hour>=12 and hour<=18:
        speak("Good Afternoon sir !")
    else:
        speak("Good evening sir ! it's a pleasent day.")

    speak("I am jarvis  . Please tell me how may I help you")

def to_day():
    # today=datetime.date.today()
    present_day =datetime.date.today()
    # Textual month, day and year	
    d2 = present_day.strftime("%B, %d, %Y")
    # print("d2 =", d2) 
    speak(f"The present date is {d2}")
    return date.today().strftime("%y-%m-%d")



def takeCommand():
    '''this function will take command
    it takes microphone input from the user and returns string output '''
    r= sr.Recognizer() 
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1  
        audio= r.listen(source)
    
    try:
        print("Recognizing.....")
        query= r.recognize_google(audio,language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        # print(e)
        print("say that again please....")
        # speak("sir , please say that again...")
        return "None "
    return query

def sendEmail(to, content):
    ob= smtplib.SMTP('smtp.gmail.com',587)
    ob.ehlo()
    ob.starttls()
    speak("sir please enter your password here: ")
    yourPass =input("enter your password here: ")
    ob.login('sid22khot@gmail.com',yourPass)
    ob.sendmail('sid22khot@gmail.com',to,content)
    ob.close()



# speak("harry is a good boy")
wishMe()

# to=['sagar22kt@gmail.com','khotsm@rknec.edu','kiteysa@rknec.edu']

while True:
# if 1:
    query= takeCommand().lower()
 

    #logic for executing tasks based on our queries /questions

    if 'wikipedia' in query:
        speak("searching wikipedia...")
        query= query.replace("wikipedia","")
        results=wikipedia.summary(query,sentences=3)
        speak("According to wikipedia...")
        print(results)
        speak(results)

    elif "open youtube" in query:
        webbrowser.open("youtube.com")
        speak("youtube has been opened")

    elif "open google" in query:
        webbrowser.open("google.com")  
        speak("google has been opened")
        

    elif "lot of time" in query:
        speak("I am really sorry from my side sir, but I'm doing my best. ")

    elif "do it fast" in query:
        speak("sure sir")

    elif " stack overflow" in query:
        speak("here you go sir")
        webbrowser.open('stackoverflow.com') 

    elif 'the time' in query:
        strTime= datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"sir, the time is {strTime} ")

    elif ('play music') in query:
        music_dir='D:\\python\\JARVIS\\music'
        songs= os.listdir(music_dir)
        print(songs)
        s1=random.randint(0,3)
        os.startfile(os.path.join(music_dir,songs[s1]))

        if 'close song' in query:
            os.close(music_dir,songs[s1])



        
        

    elif '''today's news''' in query:
        webbrowser.open('news.google.com')

    elif "what is today's date" in query:
        to_day() 

        pass

    elif "open vs code" in query:
        codePath= "C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codePath)
        speak(" here comes the vs code, sir ! ")

    # elif "email " in query:
    #     try:
    #         speak("what should I send ?")
    #         content = takeCommand()
    #         to
    #         sendEmail(to,content)
    #         speak("Email has been sent !")
    #     except Exception as e:
    #         # print(e)
    #         speak("sorry sir, I am not able to sent this email ")


    


 

    

    


    
