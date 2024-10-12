import speech_recognition as sr  # library for recognizing the speech
import webbrowser  #library for opening the links in the web browser
import pyttsx3
import musiclibrary
from openai import OpenAI
import time
import openai
import requests
from gtts import gTTS
import pygame
import os
# recognizer=sr.Recognizer
r = sr.Recognizer()
engine = pyttsx3.init('sapi5')  # here we initialize the text to speech engine 
newsapi="5d92b10a603343f3a75ea042e181620a"

def speak_old(text):
    engine.say(text)     # now we use the say function which takes the text as parameter which we want it to say
    engine.runAndWait()  # this function finally helps in executing the audio 

def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3')
    

    # Initialize pygame mixer
    pygame.mixer.init()

    # Load your MP3 file
    pygame.mixer.music.load("temp.mp3")

    # Set volume (optional)
    pygame.mixer.music.set_volume(0.7)  # Set volume from 0.0 to 1.0

    # Play the MP3 file
    pygame.mixer.music.play()

    # Keep the program running until the music finishes
    while pygame.mixer.music.get_busy():  # Check if music is still playing
        pygame.time.Clock().tick(10)      # Small delay to avoid busy-waiting
    pygame.mixer.music.stop()
    pygame.mixer.quit()
    os.remove("temp.mp3")

def aiProcess(command):
    print(command)
    client=OpenAI(
    api_key="sk-_M0vVIugVL0ChrZwQelNQOpJDxHPZqFKJiV-qqKjJ2T3BlbkFJSlo_8tXDelzNPU_1bkZh6yss3ZmiElSkM8K4OrzKAA",
)

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant named jarvis like alexa and google cloud.Give short responses"},
            {
                "role": "user",
                "content": command
            }
        ]
    )

    return completion.choices[0].message.content

def processcommand(c):
    if "open google" in c.lower():               # to open the google chrome
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():            # to open the youtube 
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():           # to open linked in
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):           # to open the music library link 
        song=c.lower().split(" ")[1]
        print(song)
        link=musiclibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        print("in news wala elif")
        # API URL
        url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}"

        # Fetch the data from the API
        response = requests.get(url)

        # Convert the response to JSON
        

        # Extract and print titles from the articles
        if response.status_code == 200:
            data = response.json()
            articles = data.get('articles',[])
            for article in articles:
               speak(article['title'])
        else:
            speak("Failed to fetch the news")

    else:
        #let api handle the request
        output=aiProcess(c)
        print(output)
        speak(output)
            
        
    print(c)



if __name__=="__main__":
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    speak("Initializing Jarvis.....")

    # listen for the wake word Jarvis
    # And speak when the Jarvis is heard
    while True:
        print("Recognizing...")
        try:
            with sr.Microphone() as source:      #here we use source variable to use microphone of the source 
                print("Say something!!!")
                audio = r.listen(source,timeout=5, phrase_time_limit=5)
            command=r.recognize_google(audio)
            if("jarvis" in command.lower()):
                speak("Ya speaking...")
                print("Google thinks you said "+command)
                with sr.Microphone() as source:
                    print("Jarvis is active, so now say open google or youtube to open them...")
                    
                    audio=r.listen(source,timeout=5, phrase_time_limit=5)
                    command=r.recognize_google(audio)
                    # speak(f"You said {command}")
                    # print("command")
                    processcommand(command)



        except sr.UnknownValueError:
            print("GOOGLE AUDIO could not understand audio")
        except sr.RequestError as e:
            print("Google AUDIO error; {0}".format(e))
