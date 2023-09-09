
import serial

ser = serial.Serial("COM6", 9600)

def SerialWrite(s):
    ser.write(s.encode())

while True:
    s = str(input())
    if "bật led" in s:
        SerialWrite('1')
    elif "tắt led" in s:
        SerialWrite('0')
    elif "nháy led" in s:
        SerialWrite('2')