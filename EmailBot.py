import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

listener = sr.Recognizer()
engine = pyttsx3.init()


email ={
    'mohit':"tihomv1995@gmail.com"
}

def talk(text):
    engine.say(text)
    engine.runAndWait()

def get_info():
    try:
        with sr.Microphone() as source:
            print('Listening.........')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass

def get_email_info():
    talk("to whom you want to send mail")
    name = get_info()
    receiver = email[name]
    talk("What is the subject of your email")
    subject = get_info()
    talk('Tell me the content')
    message = get_info()
    send_email(receiver,subject,message)



'''def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('mohitcars@gmail.com', 'mohit@9742V')
    server.sendmail('mohitcars@gmail.com',
                    'tihomv1995@gmail.com',
                    'hello')'''
def send_email(receiver,subject,message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('mohitcars@gmail.com', 'mohit@9742V')
    email =EmailMessage()
    email['From'] = 'mohitcars@gmail.com'
    email['To'] = 'tihomv1995@gmail.com'
    email['Subject'] =subject
    email.set_content(message)
    server.send_message(email)
    talk('Hey lazy your email is sent')
    talk('Do you want to send more email?')
    send_more = get_info()
    if 'yes' in send_more:
        get_email_info()

