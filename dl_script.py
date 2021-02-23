from pathlib import Path
import re
from youtube_dl import YoutubeDL
from unidecode import unidecode

def download_mp3(yt_link):
    
    if not re.match(r'((?:https?:)?\/\/)?((?:www|m)\.)?((?:youtube\.com|youtu.be))(\/(?:[\w\-]+\?v=|embed\/|v\/)?)([\w\-]+)(\S+)?',
                yt_link):
        print("Invalid URL")
        return False
    
    ydl_options = {
        'format': 'bestaudio/best',
        'ext': 'mp3',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': f'{Path.cwd()}/yt_download/%(title)s.%(ext)s',
    }

    ydl = YoutubeDL(ydl_options)
    try:
        ydl.download([yt_link])
    except:
        pass
    return True
    