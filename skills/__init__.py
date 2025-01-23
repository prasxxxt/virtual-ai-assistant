import pyttsx3
import speech_recognition as sr
import datetime


def speak(response):
    engine = pyttsx3.init()
    print(f"Fifty: {response}")
    engine.say(response)
    engine.runAndWait()


def listen():
    recognizer = sr.Recognizer()
    command = ''
    try:
        with sr.Microphone() as source:
            print('Listening...')
            audio = recognizer.listen(source=source, timeout=5, phrase_time_limit=5)
        command = recognizer.recognize_google(audio)
        print('Command : {}'.format(command))
    except sr.UnknownValueError:
        pass
    except sr.RequestError:
        print('Network error.')
    except sr.WaitTimeoutError:
        pass
    except TimeoutError:
        pass
    return command.lower()


def wish():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour <= 11:
        speak("Good morning sir")
    elif 11 <= hour <= 17:
        speak("Good afternoon sir")
    else:
        speak("Good evening sir")
    speak("fifty at your service, how can i help")

