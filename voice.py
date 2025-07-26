import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()

# Use microphone as input
with sr.Microphone() as source:
    print("Say something...")
    recognizer.adjust_for_ambient_noise(source)  # Adjust for background noise
    audio = recognizer.listen(source)  # Listen for input

    try:
        text = recognizer.recognize_google(audio)  # Convert speech to text
        print("You said:", text)
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand.")
    except sr.RequestError:
        print("Error with the service.")
