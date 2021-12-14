if __name__ == '__main__':
    clear = lambda: os.system('cls')
    from base import *
    from config import *
    
    # This Function will clean any
    # command before execution of this python file

    clear()
    assname = wishMe()
    flag = 0

    while flag == 0:
        query = takeCommand().lower()
        if query == assname:
            flag = 1
        elif query == "salir":
            speak("Adios")
            exit()

    if (uname == None):
        usernameSet()
    else:
        username(uname)

    while flag == 1:
        query = takeCommand().lower()
        # All the commands said by user will+ be
        # stored here in 'query' and will be
        # converted to lower case for easily
        # recognition of command
        if 'buscar en wikipedia' in query:
            wikipedia.set_lang("es")
            speak('Buscando en Wikipedia...')
            query = query.replace("buscar en wikipedia", "")
            results = wikipedia.summary(query, sentences = 3)
            speak("Segun Wikipedia")
            print(results)
            speak(results)

        elif "no escuches" in query or "deja de escuchar" in query or "sleep" in query:
            speak("Cuanto tiempo quieres que deje de escuchar? Dime el tiempo en segundos, y solo el número")
            a = int(takeCommand())
            speak("De acuerdo, me retiro durante " + a + (" segundos"))
            time.sleep(a)
            speak("He vuelto, estoy listo para escucharte")
            print(a)

        elif 'abrir youtube' in query:
            speak("Abriendo Youtube")
            webbrowser.open("youtube.com")

        elif 'buscar en youtube' in query:
            speak("Buscando en Youtube")
            query = query.replace("buscar en youtube", "")
            webbrowser.open("https://www.youtube.com/results?search_query=" + query)

        elif 'abrir google' in query:
            speak("Abriendo google")
            webbrowser.open("google.com")

        elif 'buscar en google' in query:
            speak("Buscando en Google. Te sientes con suerte?")
            query = query.replace("buscar en google", "")
            webbrowser.open("https://www.google.com/search?q=" + query)

        elif 'busca imágenes' in query:
            speak("Buscando en Google Imagenes")
            query = query.replace("busca imagenes", "")
            webbrowser.open("https://www.google.com/search?q=" + query + "&source=lnms&tbm=isch")

        elif 'abrir stackoverflow' in query:
            speak("Abriendo StackOverflow")
            webbrowser.open("stackoverflow.com")  

        elif 'clima de' in query or 'clima en' in query:
            speak("Buscando el" + query)
            query = query.replace("clima de", "")
            query = query.replace("clima en", "")
            api_key = WEATHERAPIKEY
            urlClima = ("http://api.openweathermap.org/data/2.5/weather?")
            complete_url = urlClima + "appid=" + api_key + "&q=" + query + "&units=metric"
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] != "404": 
                y = x["main"] 
                current_temperature = y["temp"]
                z = x["weather"] 
                weather_description = z[0]["description"]
                print("Temperatura= " +
                        str(current_temperature))
                speak("La temperatura en " + query + "es" + str(current_temperature) + "°")
            else: 
                print("No encuentro esa ciudad") 

        elif "qué es" in query or "quien es" in query:

            client = wolframalpha.Client(WOLFRAMAPIKEY)
            res = client.query(query)
            try:
                print (next(res.results).text)
                speak (next(res.results).text)
            except StopIteration:
                print ("No results")

        elif 'la hora' in query or "qué hora es" in query:
            strTime = datetime.datetime.now().strftime("%H:%M")   
            speak(f"La hora es" + strTime)

        elif "cambia mi nombre a" in query:
            query = query.replace("cambia mi nombre a", "")
            uname = query

        elif "cambiar nombre" in query:
            speak("Como te gustaria que me llame?")
            assname = takeCommand()
            speak("Gracias por darme un nombre")

        elif "dime tu nombre" in query:
            speak("Mis amigos me llaman" + assname)
            print("Mis amigos me llaman" + assname)

        elif 'salir' in query:
            speak("Gracias por usar mis servicios")
            exit()

        elif "creadores" in query or "quiénes te crearon?" in query:
            speak("Me crearon YouWannaCry, Bisdro, y Naju Testeando.")

        elif 'chiste' in query:
            speak(pyjokes.get_joke())

        elif 'enviar mensaje de whatsapp' in query:
            speak("Que mensaje quieres enviar?")
            mensaje = takeCommand()
            speak("Cuando termine esta frase, dime el numero de telefono")
            numeroT = takeCommand()
            webbrowser.open("https://api.whatsapp.com/send/?phone=" + numeroT + "&text=" + mensaje)
            pyautogui.press('enter')
            speak("Debido a limitaciones, usted tendra que enviar el mensaje, pero ya esta escrito")

        elif 'busca' in query or 'reproduce' in query:
            query = query.replace("busca", "")
            query = query.replace("reproduce", "")         
            webbrowser.open(query)

        elif 'bloquea la pantalla' in query:
                speak("Bloqueando el dispositivo")
                ctypes.windll.user32.LockWorkStation()

        elif 'apagar' in query:
                speak("Ok! Apagando el equipo en un minuto, asegurate de guardar todo antes que termine el tiempo")
                sleep(60)
                subprocess.call('shutdown /p /f')

        elif 'vaciar papelera de reciclaje' in query:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak("Papelera de reciclaje vaciada")

        elif "donde queda" in query:
            query = query.replace("donde queda", "")
            location = query
            speak("El usuario quiere saber donde queda" + location)
            webbrowser.open("https://www.google.nl/maps/place/" + location)

        elif "reiniciar" in query:
            subprocess.call("shutdown /r")

        elif "hibernar" in query or "sleep" in query:
            speak("Hibernating")
            subprocess.call("shutdown /h")

        elif "log off" in query or "cerrar sesion" in query:
            speak("Asegurate de que todas las apps esten cerradas antes de cerrar sesion")
            time.sleep(5)
            subprocess.call("shutdown /l")

        # NPPR9-FWDCX-D2C8J-H872K-2YT43
        elif assname in query:
            wishMe()
            speak(assname)