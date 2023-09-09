
from myPackage.library import *
from myPackage.speak_hear import *

# mở file question.txt và đọc file lưu các câu hỏi ở dạng list
f = open("./Project/database/question.txt", mode = "r", encoding= "utf8")          
ques = f.read().split("\n")
# Tạo hàm xử lý dữ liệu
def handle_data(text):
    # chia câu hỏi người dùng thành các từ riêng biệt
    text = text.split(" ")
    # khởi tạo lst rỗng để lưu tỉ lệ % giống nhau giữa câu hỏi người dùng và data question mình đã tạo
    ans = []

    # tính toán tỷ lệ phần trăm từng câu hỏi trong database bằng for
    for s in ques:
        # khởi tạo biến đếm số từ trùng lặp trong câu hỏi người dùng và câu hỏi trong database
        count = 0
        # tính toán số từ trùng lặp
        for i in text:
            if i in s:
                # cú mỗi lần có từ trùng lặp thì count cộng thêm 1
                count += 1
        # Sau khi tính được số từ trùng lặp thì sẽ chia cho độ dài của câu hỏi trong database để lấy tỷ lệ % trùng lặp
        ratio = count * 100 / len(s)
        # append() tỷ lệ % đó vào list
        ans.append(ratio)
    # Trả về thứ tự câu hỏi có tỷ lệ % tương ứng cao nhất
    # print(ans)
    return numpy.argmax(ans)


def ans_data(text):
    # đọc file answer.txt và lưu các câu hỏi ở dạng list
    f = open("./Project/database/answer.txt", mode= "r", encoding = "utf8")
    answer = f.read().split("\n")
    index = handle_data(text)

    speak(answer[index])


def youtube_search(text):
    # Dùng While tìm kiếm đến khi có kết quả trả về    
    while True:
        # Biến result lưu giá trị tìm được dưới dạng Dictionary
        result = YoutubeSearch(text, max_results=10).to_dict()
        if result:
            break

    url = "https://www.youtube.com/" + result[0]['url_suffix']
    webbrowser.open(url)
    time.sleep(1)
    speak("Tìm kiếm Youtube đã được hoàn thành")
