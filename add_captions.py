import os
import json
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

def add_captions(video_path, captions, output_path):
    video = VideoFileClip(video_path)
    clips = []

    for caption in captions:
        txt_clip = TextClip(caption['text'], fontsize=24, color='white', bg_color='black', size=video.size)
        txt_clip = txt_clip.set_position('bottom').set_duration(caption['duration']).set_start(caption['start'])
        clips.append(txt_clip)

    final_video = CompositeVideoClip([video] + clips)
    final_video.write_videofile(output_path, codec='libx264', audio_codec='aac')

if __name__ == "__main__":
    video_path = r"C:\Users\14064\OneDrive\Documents\school\2024Fall\Ihack\IntegrityAndMight-1\videos\your_video_id.mp4"  # Replace with your video path
    captions_path = r"C:\path\to\your\captions.json"  # Path to your JSON captions file
    output_path = r"C:\Users\14064\OneDrive\Documents\school\2024Fall\Ihack\IntegrityAndMight-1\videos\output_with_captions.mp4"

    with open(captions_path, 'r') as f:
        captions = json.load(f)

    add_captions(video_path, captions, output_path)
