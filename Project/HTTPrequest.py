
import requests as r
from myPackage.speak_hear import *
from myPackage.library import *


url = ""
s = r.get(url)

speak("Xin chào mình là trợ lý ảo Suti!!")

while True:

    you = hear()

    if you == None:
        speak("Mình chưa nghe bạn nói, bạn nói lại đi?")

    elif "bật" in you:
        if "xanh" in you:
            temp = url + "/ongreen"
            s = r.get(temp) 
            speak("Led xanh đã được bật")
        elif "vàng" in you:
            temp = url + "/onyellow"
            s = r.get(temp)  
            speak("Led vàng đã được bật")
    elif "tắt" in you:
        if "xanh" or "hai" in you:
            temp = url + "/offgreen"
            s = r.get(temp) 
            speak("Led xanh đã được tắt")
        elif "vàng" or "hai" in you:
            temp = url + "/offyellow"
            s = r.get(temp)  
            speak("Led vàng đã được tắt")