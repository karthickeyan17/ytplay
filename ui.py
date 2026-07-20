from models import Video
from utils import format_views, format_duration
from shutil import get_terminal_size
import os

def clear_screen():
    os.system('clear')

def display_results(query:str,videos:[Video])->None :
    WIDTH = get_terminal_size().columns
    print()

    print("-"*WIDTH)
    print(f"search : {query}")
    print("-"*WIDTH)

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

    print("─" * WIDTH)


def ask_choice(max_choice:int)->int|None :
    while True:
        choice = input(
                f"select [1-{max_choice}] "
                "(Enter=1,q=quit): "
                ).strip()
        if choice=="":
            return 1
        if choice.lower()=='q':
            return None
        if choice.isdigit():
            value=int(choice)
            if 1<=value<=max_choice :
                return value

        print("Invalid Choice!!!")

