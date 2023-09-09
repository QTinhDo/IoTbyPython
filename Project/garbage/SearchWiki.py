
import wikipedia
from speak import *
from hear import *
wikipedia.set_lang("vi")

def wiki_search(text):
    try:
        
        infor = wikipedia.summary(text).split('\n')
        speak(infor[0].split(".")[0])
        for a in infor[1:]:
            speak("Bạn muốn nghe thêm không")
            ans = hear()
            if "có" not in ans:
                break
            speak(a) 


        speak("Cảm ơn đã lắng nghe. Bạn muốn giúp gì nữa không")
    except:
        speak("Không tìm thấy được tài liệu bạn muốn tìm. Bạn muốn giúp gì nữa không")


