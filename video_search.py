import os
from googleapiclient.discovery import build
import yt_dlp
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

# YouTube Data API credentials
API_KEY = 'AIzaSyA5Nrkx-G0l2rvksNxn_KvEsotZzynhMtU'  # Replace with your YouTube Data API key

def search_video(query):
    youtube = build('youtube', 'v3', developerKey=API_KEY)
    
    # Search for videos matching the query
    request = youtube.search().list(
        q=query,
        part='id,snippet',
        maxResults=1,
        type='video'
    )
    response = request.execute()

    if response['items']:
        video_info = response['items'][0]
        video_id = video_info['id']['videoId']
        title = video_info['snippet']['title']
        return video_id, title
    else:
        print("No video found for the given query.")
        return None, None

def download_video(video_id, download_folder):
    video_url = f"https://www.youtube.com/watch?v={video_id}"
    print(f"Attempting to download from: {video_url}")

    ydl_opts = {
        'format': 'best',
        'outtmpl': f"{download_folder}/{video_id}.%(ext)s",
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',  # Correct the key spelling
            'preferedformat': 'mp4',  # Correct the spelling here as well
        }],
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        
        # Get the downloaded file path
        video_file_path = os.path.join(download_folder, f"{video_id}.mp4")
        # Trim the video to the first 60 seconds
        trimmed_file_path = os.path.join(download_folder, f"{video_id}_trimmed.mp4")
        ffmpeg_extract_subclip(video_file_path, 0, 60, targetname=trimmed_file_path)
        print(f"Trimmed video saved to: {trimmed_file_path}")

        # Optionally, remove the original file after trimming
        os.remove(video_file_path)

    except Exception as e:
        print(f"Error downloading video '{video_id}': {e}")
