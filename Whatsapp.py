import pywhatkit as pywhatkit
import datetime


phone ={
    'mummy':"+918126817370"
}

def whatsapp(name,msg):
    hr = int(datetime.datetime.now().strftime("%H"))
    mi = int(datetime.datetime.now().strftime("%M"))
    pywhatkit.sendwhatmsg(phone[name],msg,hr,mi+2)
