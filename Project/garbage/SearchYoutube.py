
import webbrowser
from speak import *
from youtube_search import YoutubeSearch
import time

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
