import os
from googleapiclient.discovery import build
import yt_dlp
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from dotenv import load_dotenv
import json
import subprocess

API_KEY = ""

def initialize_key():
    load_dotenv()
    global API_KEY
    API_KEY = os.getenv("YOUTUBE_API_KEY")

    if not API_KEY:
        raise ValueError("API Key not found. Make sure it's set in your environment variables.")
    
def search_video(query):
    initialize_key()
    youtube = build('youtube', 'v3', developerKey=API_KEY)
    
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
        return video_id
    else:
        print("No video found for the given query.")
        return None

def download_query_video(download_folder, outputname, query, length="00:00:20"):
    initialize_key()
    video_id = search_video(query)
    video_url = f"https://www.youtube.com/watch?v={video_id}"
    print(f"Attempting to download from: {video_url}")

    ydl_opts = {
        'format': 'best',
        'quiet': True,
        'noplaylist': True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(video_url, download=False)
        video_url = info_dict['url']

    start_time = "00:00:05"
    output_file = os.path.join(download_folder, f"{outputname}.mp4")

    ffmpeg_command = [
        'ffmpeg', '-ss', start_time, '-i', video_url, '-t', length, '-c', 'copy', output_file
    ]
    
    try:
        subprocess.run(ffmpeg_command, check=True)
        print(f"Video section saved to: {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error downloading video section: {e}")

def get_videos():
    with open(("structure.json"), 'r') as x:
        structure = json.load(x)
    
    for i in range(3):
        download_query_video("outputs/", f"yt{i+1}", structure[0][i][1])
    download_query_video("outputs/", "yt4", structure[1][1], length="00:00:59")

get_videos()