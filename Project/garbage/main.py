
from hear import *
from speak import *
from SearchWiki import *
from SearchYoutube import *
from Search import *
from datetime import date, datetime, time
import webbrowser
import time
import os

speak("Xin chào mình là trợ lý ảo Suti!!")

while True:

    you = hear()

    if you == None:
        speak("Mình chưa nghe bạn nói, bạn nói lại đi?")

    elif "tìm kiếm" in you and "thông tin" in you:
        wiki_search(you)

    # elif "tìm kiếm" in you:
    #     search(you)

    elif "tìm kiếm" in you and "video" in you:
        text = you[you.find("video")+6:]
        youtube_search(text)


    elif "hôm nay" in you or "bây giờ" in you:
        now = datetime.now()
        if "giờ" in you:
            t = now.strftime("%H h,%M phút,%S giây")
            speak(t)
        if "ngày" in you:
            t = now.strftime("Hôm nay là ngày %d, tháng %m, năm %Y")
            speak(t)    


    elif "mở" in you:
        if "facebook" in you:
            webbrowser.open("https://www.facebook.com/")
            time.sleep(1)
            speak("Facebook đã được mở")
        if "youtube" in you:
            webbrowser.open("https://www.youtube.com/")
            time.sleep(1)
            speak("Youtube đã được mở")


    elif "tạm biệt" in you:
        speak("Tạm biệt, hẹn gặp lại bạn sau")
        break