import pyttsx3

engine = pyttsx3.init()

engine.say(input("Enter your text:"))

engine.runAndWait()