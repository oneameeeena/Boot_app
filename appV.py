import speech_recognition as sr
import pyttsx3

# Initialize recognizer & voice engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Use microphone
with sr.Microphone() as source:
    print("Say something...")
    recognizer.adjust_for_ambient_noise(source)
    audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        speak(f"You said {text}")  # Bot responds
    except sr.UnknownValueError:
        speak("Sorry, I couldn't understand.")
    except sr.RequestError:
        speak("Error connecting to the service.")
