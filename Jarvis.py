import datetime
import pywhatkit as pywhatkit
import speech_recognition as sr
import pyttsx3
from word2number import w2n
from EmailBot import *
from Whatsapp import *

listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def get_order():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            info = info.lower()
            print(info)
            if 'mohit' in info:
                return info.replace('mohit','')

    except:
        pass

def start_Assist():
    talk("What you want to do")
    order = get_order()
    print(order)
    if 'play' in order:
        song = order.replace('play','')
        pywhatkit.playonyt(song)
    elif 'email' in order:
        get_email_info()
    elif 'time' in order:
        time = datetime.datetime.now().strftime("%H:%M:%S")
        talk('Current time is ' + time)
        print(time)
    elif 'whatsapp' in order:
        talk("to whom you want to send msg")
        na = get_info()
        talk("What is the mag")
        ms = get_info()
        whatsapp(na, ms)
    elif 'add' in order:
        talk("First Number")
        a = w2n.word_to_num(get_info())
        talk("Second Number")
        b = w2n.word_to_num(get_info())
        talk(a+b)
    elif 'subTect' in order:
        talk("First Number")
        a = w2n.word_to_num(get_info())
        talk("Second Number")
        b = w2n.word_to_num(get_info())
        talk(a - b)
