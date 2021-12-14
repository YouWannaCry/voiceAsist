from requirements import *
from config import *

#########################################################################
##                              Engine                                 ##
engine = pyttsx3.init('sapi5')                                         ##
voices = engine.getProperty('voices')                                  ##
engine.setProperty('voice', voices[0].id)                              ##
webbrowser.register(                                                   ##
"operagx",                                                             ##
None,                                                                  ##
webbrowser.BackgroundBrowser(                                          ##
"C://Users//arodr//AppData//Local//Programs//Opera GX//launcher.exe"), ##
preferred=True)                                                        ##
config.encoding = 'cp1251'                                             ##
#########################################################################

##Funciones##
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
 
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 6 and hour<13:
        speak("Buen día!")
  
    elif hour>= 13 and hour<19:
        speak("Buenas tardes!") 

    else:
        speak("Buenas noches!") 
  
    assname = ("yarbiss")
    print("Soy tu asistente " + assname)
    speak("Soy tu asistente " + assname)
    print("Estare en descanso hasta que digas mi nombre!")
    speak("Estare en descanso hasta que digas mi nombre!")
    return assname

def usernameSet():
    speak("Como deberia llamarte?")
    uname = takeCommand()
    return uname

def username(uname):
    speak("Bienvenido")
    columns = shutil.get_terminal_size().columns
     
    print("#####################".center(columns))
    print(f'Hola {uname}, como estas hoy?'.center(columns))
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
        print(f"El usuario dijo: {query}")
  
    except Exception as e:
        print(e)   
        print("No pude reconocer el comando.") 
        return "None"
     
    return query
  
    #Prueba del agregado de "secrets" para mantener seguras las cuentas, unames, assname, etc
    #user = config('user', default='')
    #password = config('password', default='')
    #if user != '' and password != '':
    #   connect(user, password)