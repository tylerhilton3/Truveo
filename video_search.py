import os
import json
import subprocess
from yt_dlp import YoutubeDL

def search_video(query):
    ydl_opts = {
        'format': 'best',
        'noplaylist': True,
    }

    with YoutubeDL(ydl_opts) as ydl:
        result = ydl.extract_info(query, download=False)
        if 'entries' in result:
            video_info = result['entries'][0]
            return video_info['id'], video_info['title']
        else:
            print("No video found for the given query.")
            return None, None

def download_video(video_id, download_folder):
    ydl_opts = {
        'format': 'best',
        'outtmpl': os.path.join(download_folder, f'{video_id}.mp4'),
        'noplaylist': True,
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',
        }],
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([f'https://www.youtube.com/watch?v={video_id}'])

if __name__ == "__main__":
    query = "1 minute meme"  # Your search query
    download_folder = r"C:\Users\14064\OneDrive\Documents\school\2024Fall\Ihack\IntegrityAndMight-1\videos"

    os.makedirs(download_folder, exist_ok=True)

    # Search for the video
    video_id, title = search_video(query)

    if video_id:
        # Download the video if a valid video ID was found
        download_video(video_id, download_folder)
        print(f"Video downloaded: {title}")
