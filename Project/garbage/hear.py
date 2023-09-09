# Module Hear.py

import speech_recognition as sr

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
