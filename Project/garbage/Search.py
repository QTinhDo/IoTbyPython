
import webbrowser
from speak import *
from youtube_search import YoutubeSearch
import time

def search(text):
    webbrowser.open(text)
    time.sleep(1)
    speak("Search đã được hoàn thành")
