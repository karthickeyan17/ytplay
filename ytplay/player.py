import subprocess
from .models import Video

def play(video:Video)->None:

    url = f"https://www.youtube.com/watch?v={video.id}"

    subprocess.run(
               [
                   "mpv",
                "--profile=youtube",
                url
                ]
            )
