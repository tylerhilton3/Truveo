import os
import googleapiclient.discovery
from pytube import YouTube

# Replace this with your API key
API_KEY = "AIzaSyA5Nrkx-G0l2rvksNxn_KvEsotZzynhMtU"

def search_youtube_video(query):
    # Set up YouTube API client
    youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=API_KEY)

    # Search for videos
    request = youtube.search().list(
        part="snippet",
        q=query,
        maxResults=1,
        type="video"
    )
    response = request.execute()

    if len(response['items']) > 0:
        video_id = response['items'][0]['id']['videoId']
        video_title = response['items'][0]['snippet']['title']
        return video_id, video_title
    else:
        print("No videos found.")
        return None, None

def download_video(video_id, download_folder="."):
    # Construct the YouTube video URL
    video_url = f"https://www.youtube.com/watch?v={video_id}"

    # Use pytube to download the video
    yt = YouTube(video_url)
    yt.streams.get_highest_resolution().download(download_folder)

    print(f"Downloaded video: {yt.title} to {download_folder}")

if __name__ == "__main__":
    # Search query for YouTube video
    query = "nature documentary"  # You can modify this to be dynamic

    # Search for video
    video_id, video_title = search_youtube_video(query)

    # If a video was found, download it
    if video_id:
        print(f"Found video: {video_title}")

        # Specify the download folder to save the video in your desired directory
        download_folder = r"C:\Users\14064\OneDrive\Documents\school\2024Fall\Ihack\IntegrityAndMight-1"

        # Download video to the specified folder
        download_video(video_id, download_folder)
    else:
        print("No video found.")