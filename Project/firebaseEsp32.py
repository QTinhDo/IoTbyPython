
import requests as r
from myPackage.speak_hear import *
from myPackage.library import *

url = "https://esp32-remote-4fc72-default-rtdb.firebaseio.com/.json"

json = {"green": 0, "yellow": 0}

speak("Xin chào mình là trợ lý ảo Suti!!")

while True:

    you = hear()

    if you == None:
        speak("Mình chưa nghe bạn nói, bạn nói lại đi?")

    elif "bật" in you:
        if "xanh" in you:
            json["green"] = 1
            s = r.put(url = url, json = json)
            speak("Led xanh đã được bật")
        elif "vàng" in you:
            json["yellow"] = 1
            s = r.put(url = url, json = json)
            speak("Led vàng đã được bật")
        elif "hai" in you: 
            json["green"] = 1    
            json["yellow"] = 1    
            s = r.put(url = url, json = json)    
            speak("Led xanh và led vàng đã được mở")
    elif "tắt" in you:
        if "xanh" or "hai" in you:
            json["green"] = 0
            s = r.put(url = url, json = json)
            speak("Led xanh đã được tắt")
        elif "vàng" or "hai" in you:
            json["yellow"] = 0
            s = r.put(url = url, json = json)
            speak("Led vàng đã được tắt")
        elif "hai" in you: 
            json["green"] = 0    
            json["yellow"] = 0    
            s = r.put(url = url, json = json)    
            speak("Led xanh và led vàng đã được tắt")