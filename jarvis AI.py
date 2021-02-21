import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechrecognition
import datetime
import pyaudio #pip install pyaudio
import webbrowser #pip install webbrowser
import wikipedia #pip install wikipedia
import random
import os
import requests


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("Hello my name is jarvis. what can i do for you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...") 
        speak("Say that again please...")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    
    if 1:
    
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'shutdown' in query:
            shut1 = 'ok shutting down pc'
            speak(shut1)
            print(shut1)
            os.system("shutdown /s /t 1")

        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com")
            speak("opening youtube")
        
        elif 'open word' in query:
            os.startfile('enter the path of your application')
            speak("opening word")

        elif 'open powerpoint' in query:
            os.startfile('enter the path of your application')
            speak("opening powerpoint")

    
        

        elif 'play romantic song' in query:
            webbrowser.open("https://wynk.in/music/artist/arijit-singh/arijit-singh")
            speak("playing Romantic Song")

        elif 'open google' in query:
            webbrowser.open("https://www.google.com")
            speak("opening google")
              
        elif 'open gmail' in query:
            webbrowser.open("https://mail.google.com")
            speak("opening google mail") 

        elif 'open snapdeal' in query:
            webbrowser.open("https://www.snapdeal.com") 
            speak("opening snapdeal")  

        elif 'open amazon' in query or 'shop online' in query:
            webbrowser.open("https://www.amazon.com")
            speak("opening amazon")
            
        elif 'open flipkart' in query:
            webbrowser.open("https://www.flipkart.com")
            speak("opening flipkart")
        

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   
            speak("opening stackoverflow") 

        

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'play music' in query:
            n = random.randint(0,17)
            print(n)
            music_dir = 'D:\\favmusic\\music'
            song = os.listdir(music_dir)
            print(song)
            os.startfile(os.path.join(music_dir,song[n]))
            speak("playing music")

        elif "what's up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy','i am okey ! How are you']
            ans_q = random.choice(stMsgs)
            speak(ans_q)  
            ans_take_from_user_how_are_you = takeCommand()

            if 'fine' in ans_take_from_user_how_are_you or 'happy' in ans_take_from_user_how_are_you or 'okey' in ans_take_from_user_how_are_you:
                speak('okey..')  
            elif 'not' in ans_take_from_user_how_are_you or 'sad' in ans_take_from_user_how_are_you or 'upset' in ans_take_from_user_how_are_you:
                speak('oh sorry..')  


        elif 'make you' in query or 'who create you' in query or 'develop you' in query:
            ans_m = " For your information Durvesh Satish Chopade Created me ! I give Lot of Thanks to Him "
            print(ans_m)
            speak(ans_m)
        
        elif "Ganpati Bappa" in query:
            m = "morya!"
            print(m)
            speak(m)



        elif "who are you" in query or "about you" in query or "your details" in query:
            about = "I am Jarvis an A I based computer program but i can help you lot like a your close friend ! i promise you ! Simple try me to give simple command ! like playing music or video from your directory i also play video and song from web or online ! i can also entain you i so think you Understand me ! ok Lets Start "
            print(about)
            speak(about)

        elif "hello" in query or "hello Jarvis" in query:
            hel = "Hello Durvesh Sir ! How May i Help you.."
            print(hel)
            speak(hel)

        elif "your name" in query or "sweat name" in query:
            na_me = "Thanks for Asking my name my self ! Jarvis"  
            print(na_me)
            speak(na_me)

        elif "how are you feeling" in query:
            print("feeling Very sweet after meeting with you")
            speak("feeling Very sweet after meeting with you") 

        elif 'exit' in query or 'abort' in query or 'stop' in query or 'bye jarvis' in query or 'quit' in query :
            ex_exit = 'I feeling very sweet after meeting with you but you are going! i am very sad'
            speak(ex_exit)
            exit()    
       
        elif 'open mobile' in query:
            g_url="https://web.whatsapp.com"
            results = 'opening your account'
            print(results)
            speak(results)
            webbrowser.open(g_url)

        elif 'open instagram' in query:
            g_url="https://www.instagram.com"
            results = 'opening your account'
            print(results)
            speak(results)
            webbrowser.open(g_url)

        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.com/maps/place/" + location + "")
        
        elif 'open game' in query:
            os.startfile('"D:\\jarvis\\game snake"')
            speak("opening game")

       
    
        else:
            temp = query.replace(' ','+')
            g_url="https://www.google.com/search?q="    
            res_g = 'searching google'
            print(res_g)
            speak(res_g)
            webbrowser.open(g_url+temp)

        
