from requirements import *

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
    if hour>= 6 and hour<13:
        speak("Buen día!")
  
    elif hour>= 13 and hour<19:
        speak("Buenas tardes!") 

    else:
        speak("Buenas noches!") 
  
    assname = ("diego")
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
    print('Hola, como estas hoy?'.center(columns))
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

    try:
        p = gp.getpass()
    except Exception as error:
        print('ERROR', error)
    else:
        print('Password entered')
    
    # Enable low security in gmail
    server.login('Tu email', p)
    server.sendmail('Tu email', to, content)
    server.close()