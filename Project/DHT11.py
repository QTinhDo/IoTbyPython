
import serial
from myPackage.speak_hear import *
from myPackage.library import *

ser = serial.Serial("COM6", 9600)

def SerialWrite(s):
    ser.write(s.encode())

speak("Xin chào mình là trợ lý ảo Suti!!")

while True:

    you = hear()

    if you == None:
        speak("Mình chưa nghe bạn nói, bạn nói lại đi?")


    elif "nhiệt độ" in you:
        SerialWrite('t')
        s = str(ser.readline())
        s = s[2:]
        s = s.split("\\")[0]
        speak("Nhiệt độ bây giờ là " + s + " độ C")
    elif "độ ẩm" in you:
        SerialWrite('h')
        s = str(ser.readline())
        s = s[2:]
        s = s.split("\\")[0]
        speak("Độ ẩm bây giờ là " + s + " %")


    elif "bật" in you:
        if "xanh" in you:
            SerialWrite('1')   
            speak("Led xanh đã được bật")
        elif "vàng" in you:
            SerialWrite('2')   
            speak("Led vàng đã được bật")
        elif "hai" in you:
            SerialWrite('1')   
            speak("Led xanh đã được bật")
            SerialWrite('2') 
            speak("Led vàng đã được bật")
    elif "tắt" in you:
        if "xanh" in you:
            SerialWrite('3')   
            speak("Led xanh đã được tắt")
        elif "vàng" in you:
            SerialWrite('4')   
            speak("Led vàng đã được tắt")
        elif "hai" in you:
            SerialWrite('3')   
            speak("Led xanh đã được tắt")
            SerialWrite('4') 
            speak("Led vàng đã được tắt")
    elif "nháy" in you:
        if "xanh" in you:
            SerialWrite('5')   
            speak("Led xanh đã được nháy xong")
        elif "vàng" in you:
            SerialWrite('6')   
            speak("Led vàng đã được nháy xong")
        elif "hai" in you:
            SerialWrite('5')   
            speak("Led xanh đã được nháy xong")
            SerialWrite('6') 
            speak("Led vàng đã được nháy xong")


        elif "tạm biệt" in you:
            speak("Tạm biệt, hẹn gặp lại bạn sau")
            break