import pyttsx3
import datetime
import speech_recognition as sr
import win32api, sys, os
import wikipedia 
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty("voices")
#print(i) # it will show the present default voices in your operating system
engine.setProperty('voice' , voices[2].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def paswd():
    speak("Before We start Please tell me Your Identity")
    query = take_commands().lower().strip()
    if(query == "i am abhishek" or query=="i am meliodas"):
        speak("Verification SucessFull!")
        c=1   
    else:
        speak("You are not allowed to test me") 
        c=0  
    return c     
       

def wishme():
    t = int(datetime.datetime.now().hour)
    if(t>=0 and t<=12):
        speak("Good Morning Sir.")
    elif(t>12 and t<=18):
        speak("Good Afternoon Sir. ")
    else:
        speak("Good Evening Sir.")
    speak("I am EDITH. How may i help you")    

def take_commands():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        audio = r.listen(source)
        
    try :
        print("Recognizing......")
        query = r.recognize_google(audio , language = 'Hindi')
        print("User Said:~  " + query)
    
    except Exception as e :
        print(e)
        speak("I am Not getting you , Say That Again")
        return "none"
    return query    

wishme()
c = paswd()

while c :
    speak("Give Me Some Commands")
    query = take_commands().lower()
    if 'wikipedia' in query:
        speak("Searching WEB.......")
        query = query.replace('wikipedia','')
        re = wikipedia.summary(query)
        print(re)
        speak(re)
    elif 'quit' in query:
        speak(" Quitting Sir...! Thanks for your time :)")
        c=0    
    elif 'open youtube' in query:
        speak("here we go..")
        webbrowser.open("youtube.com")  
    elif 'about you' in query:
        speak(" i am managed by an awesome person , and I am trying to get smarter day by day . you can find my source code at github")
    elif 'play music' in query:
        speak(" i didn't got this knowledge So far") 
    elif 'black cat' in query:
        speak("Meliodas is best friend of My Creator and i am allowed to verified by him also")      
    elif 'google it' in query:
        speak("Sure!!!")
        query = query.replace("search google","")
        re = webbrowser.open("google.com/"+query)
