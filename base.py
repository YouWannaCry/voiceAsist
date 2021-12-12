import subprocess
import wolframalpha
import pyttsx3
import tkinter
import json
import random
import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import winshell
import pyjokes
import feedparser
import smtplib
import ctypes
import time
import requests
import shutil
from twilio.rest import Client
from clint.textui import progress
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen

##############################################
##                Engine                    ##
engine = pyttsx3.init('sapi5')              ##
voices = engine.getProperty('voices')       ##
engine.setProperty('voice', voices[0].id)   ##
webbrowser.register("operagx",None,webbrowser.BackgroundBrowser("C://Users//arodr//AppData//Local//Programs//Opera GX//launcher.exe"),preferred=True)
##############################################

##Funciones##
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
 
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak("Buen dia!")
  
    elif hour>= 12 and hour<18:
        speak("Buenas tardes!")  
  
    else:
        speak("Buenas noches!") 
  
    assname =("Jarvis")
    speak("Soy tu asistente" + assname)

def usernameSet():
    speak("Como deberia llamarte?")
    uname = takeCommand()
    return uname

def username(uname):
    speak("Bienvenido")
    speak(uname)
    columns = shutil.get_terminal_size().columns
     
    print("#####################".center(columns))
    print('Hola, como estas hoy? uname'.center(columns))
    print("#####################".center(columns))
     
    speak("Como puedo ayudarte hoy?")
 
def takeCommand():
     
    r = sr.Recognizer()
     
    with sr.Microphone() as source:
         
        print("Escuchando...")
        r.pause_threshold = 1
        audio = r.listen(source)
  
    try:
        print("Pensando...")   
        query = r.recognize_google(audio, language ='es-AR')
        print(f"User said: {query}/n")
  
    except Exception as e:
        print(e)   
        print("No pude reconocer el comando.") 
        return "None"
     
    return query
  
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
     
    # Enable low security in gmail
    server.login('Tu email', 'Tu password')
    server.sendmail('Tu email', to, content)
    server.close()
