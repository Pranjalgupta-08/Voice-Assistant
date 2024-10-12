import pyttsx3

def speak_with_all_voices(text):
    # Initialize the pyttsx3 engine with 'sapi5' for Windows systems
    engine = pyttsx3.init('sapi5')
    
    # Get available voices
    voices = engine.getProperty('voices')

    # Iterate over the available voices
    for idx, voice in enumerate(voices):
        print(f"Using Voice: {voice.name}")
        engine.setProperty('voice', voice.id)
        
        # Speak the text using the current voice
        engine.say(f"Voice {idx+1}: {text}")
        engine.runAndWait()

if __name__ == "__main__":
    text_to_speak = "The quick brown fox jumped over the lazy dog."
    speak_with_all_voices(text_to_speak)
