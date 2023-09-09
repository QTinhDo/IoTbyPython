
import requests as r
from gtts import gTTS
import playsound
import os
import speech_recognition as sr

def speak(text):
    print("Suti: " + text)
    tts = gTTS(text=text, lang="vi", slow=False)              # Chuyển text thành âm thanh qua API Google
    tts.save("./Project/sound.mp3")                           # Lưu lại âm thanh thành sound.mp3
    playsound.playsound("./Project/sound.mp3", True)          # Phát file sound.mp3
    os.remove("./Project/sound.mp3")                          # Xóa file sound.mp3


def hear():
    print("Đang nghe:.....")
    r = sr.Recognizer() 
    # source = sr.Microphone()
    with sr.Microphone() as source:
        audio = r.listen(source, phrase_time_limit= 3)  # Mở một micro mới với tên source sau khi thoát with as thì tắt micro đi
        try:
            text = r.recognize_google(audio, language="vi-VN")  # Lưu câu nói dưới dạng âm thanh (.mp3)
            print("Tôi: " + text)
            return str(text).lower()
        except:
            return None

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

    elif "tạm biệt" in you:
        speak("Tạm biệt, hẹn gặp lại bạn sau")
        break