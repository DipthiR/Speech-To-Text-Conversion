import speech_recognition as sr

recognizer = sr.Recognizer()

print(" Speech-to-Text is running... Say 'stop listening' to exit.")

while True:
    try:
        with sr.Microphone() as source:
            print("\nSpeak Now...")
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = recognizer.listen(source)

            text = recognizer.recognize_google(audio)
            print(" You said:", text)

            if text.lower() == "stop listening":
                print(" Exiting speech recognition loop.")
                break

    except sr.UnknownValueError:
        print(" Could not understand your speech.")
    except sr.RequestError:
        print(" Could not request results from the speech service.")
    except KeyboardInterrupt:
        print("\n Manually stopped.")
        break
