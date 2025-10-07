import pyttsx3

engine = pyttsx3.init()

print("Welcome to Robospeaker. Type 'exit' to quit.")

while True:
    text = input("Enter what you want me to speak: ")
    if text.lower() == "exit":
        print("Goodbye!")
        break
    engine.say(text)
    engine.runAndWait()
