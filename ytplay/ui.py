from models import Video
from utils import format_views, format_duration
from shutil import get_terminal_size
import os

WIDTH = get_terminal_size().columns

def clear_screen():
    os.system('clear')

def hLine():
    print("-"*WIDTH)

def display_results(query:str,videos:[Video])->None :
    print()

    hLine()
    print(f"search : {query}")
    hLine()

    for index, video  in enumerate(videos, start=1):
        print(f"{index:2} │ {video.title}")
        print(
            f"   │ "
            f"{video.channel:<35}"
            f"{format_views(video.views):>8}"
            f"   "
            f"{format_duration(video.duration):>5}"
        )
        print()

    hLine()

def ask_choice(videos:list[Video])->Video|None :
    while True:
        choice = input(
                f"select [1-{len(videos)}] "
                "(Enter=1,q=quit): "
                ).strip()
        if choice=="":
            return videos[0]
        if choice.lower()=='q':
            return None
        if choice.isdigit():
            value=int(choice)
            if 1<=value<=len(videos) :
                return videos[value-1]

        print("Invalid Choice!!!")

