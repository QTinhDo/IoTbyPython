from myPackage.library import *

# ModulemyGUI.py
# đồ họa
root = Tk()
root.title("Virtual Assistant")                     # Đặt tên tiêu đề
root.geometry("900x830")                            # Cài độ rộng cho background
root.iconbitmap("./Project/data_dohoa\\logo.ico")             # Chèn logo vào giao diện

load = Image.open("./Project/data_dohoa\\background.jpg")     # Chèn background vào giao diện
render = ImageTk.PhotoImage(load)                   # Biến render giúp xuất background ra ngoài
img = Label(root, image = render)                   # lable giúp hiển thị hình ảnh và văn bản
img.place(x = 0, y = 0)                             # đặt background lên màn hình

# tạo biến Label để giúp hiển thị chữ ra màn hình
name = Label(root, text = "VIRTUAL ASSISTANT", fg = '#45F848', bd = 0, bg = "#03152D") 
name.config(font = ("Transformers Movie", 35))      # cấu hình dùng font transformers Movie với cỡ chữ 35
name.pack(pady = 10)  

# box 1
# Tương tự tạo Label name1 hiển thị chữ  "ANNA HEAR" lên background
name1 = Label(root, text = "SUTI HEAR", fg = '#F8E245', bd = 0, bg = "#03152D")
name1.config(font = ("Transformers Movie", 20))
name1.pack(pady = 30)

# tạo một ô để hiển thị nội dung trợ lý ảo nghe được ra giao diện
box1 = Text(root, width = 48, height = 8, font = ("ROBOTO", 16))
box1.pack(pady = 0)

# box2
# Tạo Label hiện thị text "ANNA SPEAK" lên background
name2 = Label(root, text = "SUTI SPEAK", fg = '#F8E245', bd = 0, bg = "#03153D")
name2.config(font = ("Transformers Movie", 20))
name2.pack(pady = 30)

# tạo ô để hiện thị nội dung trợ lý ảo speak ra giao diện
box2 = Text(root, width = 48, height = 8, font = ("ROBOTO", 16))
box2.pack(pady = 0)

# Tạo hàm để xuất text ra box tương ứng đã tạo ở trên
def hear_(text):
    box1.delete(1.0, END)       # xóa nội dung cũ trong box1
    box1.insert(END, text)      # viết nội dung mới vào box1
def speak_(text):
    box2.delete(1.0, END)       # xóa nội dung cũ trong box2
    box2.insert(END, text)      # viết nội dung mới vào box2




# Module Speak.py
def speak(text):
    print("Suti: " + text)
    speak_(text)
    tts = gTTS(text=text, lang="vi", slow=False)              # Chuyển text thành âm thanh qua API Google
    tts.save("./Project/sound.mp3")                           # Lưu lại âm thanh thành sound.mp3
    playsound.playsound("./Project/sound.mp3", True)          # Phát file sound.mp3
    os.remove("./Project/sound.mp3")                          # Xóa file sound.mp3


# Module Hear.py
def hear():
    print("Đang nghe:.....")
    r = sr.Recognizer() 
    # source = sr.Microphone()
    with sr.Microphone() as source:
        audio = r.listen(source, phrase_time_limit= 3)  # Mở một micro mới với tên source sau khi thoát with as thì tắt micro đi
        try:
            text = r.recognize_google(audio, language="vi-VN")  # Lưu câu nói dưới dạng âm thanh (.mp3)
            print("Tôi: " + text)
            hear_(text)
            return str(text).lower()
        except:
            return None
