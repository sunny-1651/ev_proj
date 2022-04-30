import pyttsx3
import speech_recognition as sr
import random
import datetime
import cv2
import mediapipe as mp

engine = pyttsx3.init()
newVoiceRate = 115
engine.setProperty('rate',newVoiceRate)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def improcess(img):
    mpHands = mp.solutions.hands
    hands = mpHands.Hands()
    mpDraw = mp.solutions.drawing_utils
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    h, w, c = img.shape
    cv2.line(img, (0,0), (w,h), (255,0,0), 2)
    cv2.line(img, (w,0), (0,h), (255,0,0), 2)
    return results, img, h, w

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def check(a, b, c, d, x, y):
    return ((c - a)*(y - b) - (d - b)*(x - a)) > 0

def position(b1, b2):
    if (b1 and b2):
        return "right"
    elif (b1 and ~b2):
        return "back"
    elif (b1 == False and b2 == False):
        return "left"
    elif (b1 == False and b2 == True):
        return "forward"
    else:
        return "Some error occured"

def wishMe():
    sal = ["hey", "hey buddy", "hey budd,", "hi", "hello", "hello, how are you", "howdy", "howdy, mate"]
    speak(random.choice(sal))
    hour = int(datetime.datetime.now().hour)
    if hour >= 5 and hour < 12:
        speak("Good Morning")

    elif hour >= 12 and hour < 16:
        speak("Good Afternoon")

    elif hour >= 16 and hour < 19:
        speak("Good Evening")

    speak("lets get the wheels rolling whoom whoom")

def takeCommand(x = "Listening..."):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(x)
        # r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en')
        print("User said: {query} \n")

    except Exception as e:
        print("I was unable to transcribe that, Could you repeat it please")
        return "None"
    return query

# if __name__ == "__main__":
#     while True:
#         query = takeCommand().lower()
#         print("pt 1")
#         if "scooby" in query:
#             query = query.replace("scooby ", "")
#             print(query)
