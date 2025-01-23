# Importing required libraries and functions
import sys
import webbrowser as wb
import json
import wikipedia
from requests import get
import os
from skills import speak, listen
import pywhatkit as kit


# Defining get funtion to find tasks to do using predicted intent
def get_function(intent, command, response):
    if intent == "greeting":
        greeting(response)
    elif intent == "introduction":
        introduction(response)
    elif intent == "say":
        say(command)
    elif intent == "applications":
        application(command, response)
    elif intent == "google_search":
        google_search(command, response)
    elif intent == "wikipedia_search":
        wikipedia_search(command)
    elif intent == "youtube_search":
        youtube_search(command)
    elif intent == "home_automation":
        home_automation(command, response)
    elif intent == "ip_address":
        ip_address(response)
    elif intent == "shutdown":
        shutdown(command, response)


# Defining greeting function
def greeting(response):
    speak(response)


# Defining introduction function
def introduction(response):
    speak(response)


# Defining say function
def say(command):
    if "say" in command or "speak" in command:
        command = command.replace("say", "").replace("speak", "")
        speak(command)

# Defining application and websites function
def application(command, response):
    with open('data/apps.json') as file:
        data = json.load(file)
    if "open" in command or "launch" in command or "run" in command:
        for app in data['apps']:
            if app in command:
                os.startfile(data["apps"][app])
                speak(response)
        for app in data['sites']:
            if app in command:
                os.startfile(data["sites"][app])
                speak(response)
    elif "close" in command or "terminate" in command or "quit" in command:
        for app in data['apps']:
            if app in command:
                address = data["apps"][app].split("\\")
                appname = address[len(address) - 1]
                os.system(f"taskkill /f /im {appname}")
                speak(response)
        for app in data['sites']:
            if app in command:
                os.system("taskkill /f /im chrome.exe")
                speak(response)


# Defining google search function
def google_search(command, response):
    speak("what do you like to search")
    keyword = listen()
    wb.open(f"https://www.google.com/search?q={keyword}")
    speak(response)


# Defining wikipedia search function
def wikipedia_search(command):
    command = command.replace("wikipedia", "")
    result = wikipedia.summary(command, sentences=2)
    speak(f"according to wikipedia {result}")
    speak("sir is there anything else i can do")


# Defining youtube search function
def youtube_search(command):
    if "song" in command or "music" in command:
        speak("which song you like to play")
        song_name = listen().lower()
        speak(f"playing {song_name} on youtube, enjoy")
        kit.playonyt(song_name)
    if "video" in command or "videos" in command:
        speak("which video you like to play")
        video = listen().lower()
        speak(f"playing {video} on youtube, enjoy")
        kit.playonyt(video)


# Defining home automation function
def home_automation(command, response):
    if "light" in command or "bulb" in command or "lights" in command or "bulbs" in command:
        if "on" in command:
            get("http://192.168.1.4/0/on")
            get("http://192.168.1.4/1/on")
            get("http://192.168.1.4/2/on")
            get("http://192.168.1.4/3/on")
            speak("lights are on now")
            speak(response)
        elif "off" in command:
            get("http://192.168.1.4/0/off")
            get("http://192.168.1.4/1/off")
            get("http://192.168.1.4/2/off")
            get("http://192.168.1.4/3/off")
            speak("lights are off now")
            speak(response)
    elif "fan" in command:
        if "on" in command:
            get('http://192.168.1.4/5/on')
            speak("fan is on now")
            speak(response)
        elif "off" in command:
            get("http://192.168.1.4/5/off")
            speak("fan is off now")
            speak(response)
    else:
        speak("sorry i did not understand home automation command")


# Defining ip address function
def ip_address(response):
    ip = get('https://api.ipify.org').text
    speak(f"Our Systems IP address is {ip}")
    speak(response)


# Defining shutdown function
def shutdown(command, response):
    if "50" in command or "fifty" in command:
        speak("system shutdown initiated")
        speak(response)
        sys.exit(0)

