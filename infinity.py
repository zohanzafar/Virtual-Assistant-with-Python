import speech_recognition as sr  #recognise speech
import playsound  # to play an audio file
from gtts import gTTS  # google text to speech
import random
from time import ctime  # get time details
import webbrowser  # open browser
import time
import os  # to remove created audio files
import pyautogui
import pyttsx3  # text to speech
import pywhatkit
from tkinter import *
from PIL import Image
import pyjokes
import pandas as pd
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB

class person:
    name = ''
    def setName(self, name):
        self.name = name

class infinity:
    name = ''
    def setName(self, name):
        self.name = name

def there_exists(terms):
    for term in terms:
        if term in voice_data:
            return True


def engine_speak(text):
    text = str(text)
    engine.say(text)
    engine.runAndWait()

r = sr.Recognizer()  # initialise a recogniser

# listen for audio and convert it to text:
def record_audio(ask=""):
    with sr.Microphone(1) as source:  # microphone as source
        if ask:
            engine_speak(ask)
        audio = r.listen(source, 5, 5)  # listen for the audio via source
        print("Done Listening")
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)  # convert audio to text
        except sr.UnknownValueError:  # error: recognizer does not understand
            engine_speak('I did not get that')
        except sr.RequestError:
            engine_speak('Sorry, the service is down')  # error: recognizer is not connected
        print(">>", voice_data.lower())  # print what user said
        return voice_data.lower()

# get string and make a audio file to be played
def engine_speakk(audio_string):
    audio_string = str(audio_string)
    tts = gTTS(text=audio_string, lang='en')  # text to speech(voice)
    r = random.randint(1, 20000000)
    audio_file = 'audio' + str(r) + '.mp3'
    tts.save(audio_file)  # save as mp3
    playsound.playsound(audio_file)  # play the audio file
    print(infinity_obj.name + ":", audio_string)  # print what app said
    os.remove(audio_file)  # remove audio file

def respond(voice_data):

    # 1: greeting
    if there_exists(['hey', 'hi', 'hello']) and 'weather' not in voice_data:
        greetings = ["hey, how can I help you" + person_obj.name, "hey, what's up?" + person_obj.name,
                     "I'm listening" + person_obj.name, "how can I help you?" + person_obj.name,
                     "hello" + person_obj.name]
        greet = greetings[random.randint(0, len(greetings) - 1)]
        engine_speak(greet)

    # 2: name
    if there_exists(["what is your name", "what's your name", "tell me your name"]):
        if person_obj.name:
            engine_speak(f"My name is {infinity_obj.name}, {person_obj.name}")  # gets users name from voice input
        else:
            engine_speak(f"My name is {infinity_obj.name}. what's your name?")  # incase you haven't provided your name.

    if there_exists(["my name is"]):
        person_name = voice_data.split("is")[-1].strip()
        engine_speak("okay, i will remember that " + person_name)
        person_obj.setName(person_name)  # remember name in person object

    if there_exists(["what is my name"]):
        engine_speak("Your name must be " + person_obj.name)

    if there_exists(["your name should be"]):
        infinity_name = voice_data.split("be")[-1].strip()
        engine_speak("okay, i will remember that my name is " + infinity_name)
        infinity_obj.setName(infinity_name)  # remember name in object

    # 3: greeting
    if there_exists(["how are you", "how are you doing"]):
        engine_speak("I'm very well, thanks for asking " + person_obj.name)

    # 4: time
    if there_exists(["what's the time", "tell me the time", "what time is it", "what is the time"]):
        time = ctime().split(" ")[3].split(":")[0:2]
        if time[0] == "00":
            hours = '12'
        else:
            hours = time[0]
        minutes = time[1]
        time = hours + " hours and " + minutes + " minutes"
        engine_speak(time)

    # 5: search google
    if there_exists(["search for"]) and 'youtube' not in voice_data:
        search_term = voice_data.split("for")[-1]
        url = "https://google.com/search?q=" + search_term
        webbrowser.get().open(url)
        engine_speak("Here is what I found for" + search_term + "on google")

    if there_exists(["search"]) and 'youtube' and 'for' not in voice_data:
        search_term = voice_data.replace("search", "")
        url = "https://google.com/search?q=" + search_term
        webbrowser.get().open(url)
        engine_speak("Here is what I found for" + search_term + "on google")

    # 6: search youtube
    if there_exists(["youtube"]):
        search_term = voice_data.split("for")[-1]
        search_term = search_term.replace("on youtube", "").replace("search", "")
        url = "https://www.youtube.com/results?search_query=" + search_term
        webbrowser.get().open(url)
        engine_speak("Here is what I found for " + search_term + "on youtube")

    # 7: play on youtube
    if there_exists(["play"]):
        search_term = voice_data.split("play")[-1]
        pywhatkit.playonyt(search_term)
        engine_speak("playing " + search_term + " on youtube")

    # 8: get stock price
    if there_exists(["price of"]):
        search_term = voice_data.split("for")[-1]
        url = "https://google.com/search?q=" + search_term
        webbrowser.get().open(url)
        engine_speak("Here is what I found for " + search_term + " on google")

    # 9: time table
    if there_exists(["show my time table"]):
        im = Image.open(r"C:\Users\xeoncity\Downloads\pythonAiProject\TimeTable.jpeg")
        im.show()
        engine_speak("showing the timetable")

    # 10: weather
    if there_exists(["weather"]) and 'temperature' not in voice_data:
        search_term = voice_data.split("of")[-1]
        url = "https://www.google.com/search?q="+search_term+"+weather&ei=0YewYujZJLmQxc8PsNeu0Ao&ved=0ahUKEwiohrijorz4AhU5SPEDHbCrC6oQ4dUDCA4&uact=5&oq=karachi+weather&gs_lcp=Cgdnd3Mtd2l6EAMyDQgAEIAEELEDEEYQgAIyCwgAEIAEELEDEIMBMgsIABCABBCxAxCDATILCAAQgAQQsQMQgwEyDggAEIAEELEDEIMBEMkDMgUIABCSAzIICAAQgAQQsQMyCwgAEIAEELEDEIMBMgsIABCABBCxAxCDATILCAAQgAQQsQMQgwE6BAgAEEc6CggAELEDEIMBEEM6BAgAEEM6BAguEEM6CwguEIAEELEDEIMBOggIABCxAxCDAToICAAQgAQQyQM6BQguEJECOgUIABCRAjoLCC4QxwEQ0QMQkQI6BQgAEIAEOgcIABCxAxAKOgoIABCxAxCDARAKOgwIABCxAxAKEEYQgAI6DQgAELEDEIMBEMkDEApKBAhBGABKBAhGGABQ7wRYz0ZgwUloCXACeAGAAcgCiAHyFJIBBzAuNi40LjKYAQCgAQHIAQjAAQE&sclient=gws-wiz"
        webbrowser.get().open(url)
        engine_speak("Here is what I found for " + search_term + " on google")

    # 11: playing prediction
    if there_exists(["temperature"]):
        try:
            search_term = voice_data.split("weather")[-1]
            w = search_term.split("and")[0]
            t = search_term.split("is")[-1]
            weather = ['sunny', 'sunny', 'overcast', 'rainy', 'rainy', 'rainy', 'overcast', 'sunny', 'sunny', 'rainy','sunny', 'overcast', 'overcast', 'rainy']
            temperature = ['hot', 'hot', 'hot', 'mild', 'cool', 'cool', 'cool', 'mild', 'cool', 'mild', 'mild', 'mild','hot', 'mild']
            play = ['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No']
            w1 = weather.index(w.strip())
            t1 = temperature.index(t.strip())
            le = preprocessing.LabelEncoder()
            weather_encoded = le.fit_transform(weather)
            temperature_encoded = le.fit_transform(temperature)
            label = le.fit_transform(play)
            w2 = weather_encoded[w1]
            t2 = temperature_encoded[t1]
            features = list(zip(weather_encoded, temperature_encoded))
            model = KNeighborsClassifier(n_neighbors=3, metric='euclidean')
            model.fit(features, label)
            prediction = model.predict([[w2, t2]])
            a = le.inverse_transform(prediction)
            p = a[0]
            if p == 'Yes':
                engine_speak(p + " you can go outside")
            else:
                engine_speak(p + " you can not go outside")
        except ValueError as v:
            engine_speak("You have entered wrong information")

    # 12: stone paper scisors
    if there_exists(["game"]):
        voice_data = record_audio("choose among rock paper or scissor")
        moves = ["rock", "paper", "scissor"]
        cmove = random.choice(moves)
        pmove = voice_data
        engine_speak("The computer chose " + cmove)
        engine_speak("You chose " + pmove)
        if pmove == cmove:
            engine_speak("the match is draw")
        elif pmove == "rock" and cmove == "scissor":
            engine_speak("Player wins")
        elif pmove == "rock" and cmove == "paper":
            engine_speak("Computer wins")
        elif pmove == "paper" and cmove == "rock":
            engine_speak("Player wins")
        elif pmove == "paper" and cmove == "scissor":
            engine_speak("Computer wins")
        elif pmove == "scissor" and cmove == "paper":
            engine_speak("Player wins")
        elif pmove == "scissor" and cmove == "rock":
            engine_speak("Computer wins")

    # 13: toss a coin
    if there_exists(["toss", "flip", "coin"]) and 'of' not in voice_data:
        moves = ["head", "tails"]
        cmove = random.choice(moves)
        engine_speak("The computer choose " + cmove)

    # 14: calc
    if there_exists(["plus", "minus", "multiply", "divide", "power", "+", "-", "*", "/"]):
        try:
            opr = voice_data.split()[1]
            if opr == '+':
                engine_speak(int(voice_data.split()[0]) + int(voice_data.split()[2]))
            elif opr == '-':
                engine_speak(int(voice_data.split()[0]) - int(voice_data.split()[2]))
            elif opr == 'multiply' or 'x':
                engine_speak(int(voice_data.split()[0]) * int(voice_data.split()[2]))
            elif opr == 'divide':
                engine_speak(int(voice_data.split()[0]) / int(voice_data.split()[2]))
            elif opr == 'power':
                engine_speak(int(voice_data.split()[0]) ** int(voice_data.split()[2]))
            else:
                engine_speak("Wrong Operator")
        except IndexError:
            engine_speak('you have entered wrong information')

    # 15: screenshot
    if there_exists(["capture", "my screen", "screenshot"]):
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save('C:/Users/Tooba Zafar/Downloads/pythonAiProject/pythonAiProject/ScreenShot/ss.png')
        engine_speak("screenshot taken")


    # 16: Ip Address
    if there_exists(["what is my ip"]):
        url = "https://www.where-am-i.co/my-ip-location"
        webbrowser.get().open(url)
        engine_speak("finding you ip address")

    # 17: Current location as per Google maps
    if there_exists(["what is my exact location"]):
        url = "https://www.google.com/maps/search/Where+am+I+?/"
        webbrowser.get().open(url)
        engine_speak("You must be somewhere near here, as per Google maps")

    # 18: About diseases
    if there_exists(["tell me about"]):
        try:
            search_term = voice_data.split("about")[-1]
            i2 = search_term
            dataset = pd.read_csv('diseases_description.csv')
            feature1 = dataset['T']
            feature2 = dataset['Diseases']
            label = dataset['Description']
            diseases = ['drug reaction', 'malaria', 'allergy', 'hypothyroidism', 'psoriasis', 'gerd', 'chronic cholestasis','hepatitis a', 'osteoarthristis', 'paroymsal positional vertigo', 'hypoglycemia', 'acne','diabetes', 'impetigo', 'hypertension', 'peptic ulcer diseae', 'dimorphic hemorrhoids ','common cold', 'chicken pox', 'cervical spondylosis', 'hyperthyroidism', 'urinary tract infection','varicose veins', 'aids', 'paralysis', 'typhoid', 'hepatitis b', 'fungal infection', 'hepatitis c','migraine', 'bronchial asthma', 'alcoholic hepatitis', 'jaundice', 'hepatitis e', 'dengue','hepatitis d', 'heart attack', 'pneumonia', 'arthritis', 'gastroenteritis', 'tuberculosis']
            input2 = diseases.index(i2.strip())
            le = preprocessing.LabelEncoder()
            f1_encoded = le.fit_transform(feature1)
            f2_encoded = le.fit_transform(feature2)
            label_encoded = le.fit_transform(label)
            features = list(zip(f1_encoded, f2_encoded))
            model = GaussianNB()
            model.fit(features, label)
            inputone = 0
            inputtwo = f2_encoded[input2]
            pred = model.predict([[inputone, inputtwo]])
            engine_speak(pred)
        except ValueError as v:
            engine_speak("You have entered wrong information")

    # 19: Joke
    if there_exists(["tell me a joke"]):
        engine_speak(pyjokes.get_joke())

    # 20: Exit
    if there_exists(["exit", "quit", "goodbye"]):
        engine_speak("bye.")
        os.system("taskkill /im msedge.exe /f")
        exit()

time.sleep(1)
webbrowser.open_new_tab('index.html')
person_obj = person()
infinity_obj = infinity()
infinity_obj.name = 'infinity'
person_obj.name = 'zohan'
engine = pyttsx3.init()

while (1):

    voice_data = record_audio("Recording")  # get the voice input
    print("Done")
    print("Q:", voice_data)
    respond(voice_data)