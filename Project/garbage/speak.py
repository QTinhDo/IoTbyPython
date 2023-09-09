
from gtts import gTTS
import playsound
import os


def speak(text):
    print("Suti: " + text)
    tts = gTTS(text=text, lang="vi", slow=False)              # Chuyển text thành âm thanh qua API Google
    tts.save("./Project/sound.mp3")                           # Lưu lại âm thanh thành sound.mp3
    playsound.playsound("./Project/sound.mp3", True)          # Phát file sound.mp3
    os.remove("./Project/sound.mp3")                          # Xóa file sound.mp3


