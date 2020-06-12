import pyttsx3
import speech_recognition as sr
import wikipedia
import datetime
import webbrowser
import os


engine=pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
     hour= int(datetime.datetime.now().hour)
     if hour>=0 and hour<12:
         speak("Good Morning")

     elif  hour>=12 and hour<18:
         speak("Good Afternoon")

     else:
         speak("Good Evening")

     speak("Hello sir i am jarvis how may i help you")   

def takeCommand():

     r = sr.Recognizer()

     with sr.Microphone() as source:
         print("Listening........")
         r.pause_threshold=1
         audio=r.listen(source)

     try:
         print("Recognizing")
         query = r.recognize_google(audio, language='en-in')
         print(f"User said: {query}\n")

     except Exception as e:
        print(e)
        
        print("Say that again please")

        return "None"
     return query
if __name__ == "__main__":
    wishMe()

    
    query=takeCommand().lower()

    if 'wikipedia' in query:
       speak('Searching wikipedia...')
       query=query.replace("wikipedia", "")
       results=wikipedia.summary(query, sentences=2)
       speak('According to wikipedia')
       speak(results)

    elif 'youtube' in query:
       webbrowser.open("youtube.com")

    elif 'google' in query:
       webbrowser.open("google.com")

    elif 'music' in query:
       music_dir='Path'
       songs=os.listdir(music_dir)
       os.startfile(os.path.join(music_dir,songs[0])) 
