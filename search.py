import yt_dlp
#from pprint import pprint
from models import Video

def search(keyword: str, limit: int=10) -> list[Video]:
    opts = {
            'skip_download': True,
            'quit':True,
            'extract_flat':True,
            "no_warnings": True,
            "noprogress": True,
            }
    with yt_dlp.YoutubeDL(opts) as obj:
        result = obj.extract_info(
                f"ytsearch{limit}:{keyword}",
                download=False,
                )

    videos = []

    for entry  in result.get('entries',[]):
        #pprint(entry)
        #break
        videos.append(
                Video(
                    id=entry.get('id',""),
                    title=entry.get('title',""),
                    channel=entry.get('channel') or entry.get('uploader') or 'unknown',
                    duration=entry.get('duration') or 0,
                    views=entry.get('view_count') or 0,
                    )
                )
    return videos
