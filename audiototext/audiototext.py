import speech_recognition as sr

recognizer = sr.Recognizer()
recognizer.energy_threshold = 500
mic = sr.Microphone()

def recorder():
    with mic as source:
        print("Please speak to your microphone.")
        recognizer.adjust_for_ambient_noise(source)
        print("Ready.")
        audio = recognizer.listen(source)
        print("Audio captured.")
        try:
            text = recognizer.recognize_google(audio)
            print("Your text is\n*******************************")
            print(text)
            print("*******************************")
        except sr.UnknownValueError:
            print("Program didn't understand you. Please speak again.")
        except sr.RequestError:
            print("Program down.")

def main():
    x = input("Press 1 to start program\nPress 2 to end program.\n")
    while x == "1":
        recorder()
        main()   
    if x == "2":
        print("Turning off..")


main()

    
