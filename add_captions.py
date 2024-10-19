from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
import json

def add_captions_with_timing(video_path, json_path, output_path):
    # Load the video
    video_clip = VideoFileClip(video_path)

    # Load the JSON script
    with open(json_path, 'r') as f:
        script = json.load(f)

    # Create a list to store all the caption clips
    caption_clips = []

    # Define caption settings (position, font, size, color, etc.)
    caption_settings = {
        'fontsize': 40,
        'color': 'white',
        'position': 'bottom',  # You can change this to 'top', 'center', etc.
        'font': 'Arial-Bold'  # Pick a font that works for your system
    }

    # Adding captions from script[0] (3 parts)
    duration_per_caption = video_clip.duration / len(script[0])  # Distribute evenly

    for i, sentence in enumerate(script[0]):
        # Create a text caption for each script line (use sentence[0] for the text)
        caption_text = sentence[0]
        caption_clip = TextClip(caption_text, **caption_settings)
        caption_clip = caption_clip.set_start(i * duration_per_caption).set_duration(duration_per_caption)
        caption_clips.append(caption_clip)

    # Add credibility ratings if present in script[1]
    if len(script) > 1 and isinstance(script[1], list):
        credibility_lines = script[1][1]  # Assume script[1][1] holds the credibility lines
        for i, cred_text in enumerate(credibility_lines[:3]):
            # Set a duration and start time for credibility captions (after the main script is done)
            start_time = (len(script[0]) + i) * duration_per_caption
            cred_caption_clip = TextClip(cred_text, **caption_settings)
            cred_caption_clip = cred_caption_clip.set_start(start_time).set_duration(duration_per_caption)
            caption_clips.append(cred_caption_clip)

    # Combine the original video with the caption clips
    final_video = CompositeVideoClip([video_clip] + caption_clips)

    # Write the final video with captions to output path
    final_video.write_videofile(output_path, codec="libx264")

# Usage example
video_path = "videos\.mp4"
json_path = "path_to_json_script.json"
output_path = "final_video_with_captions.mp4"
add_captions_with_timing(video_path, json_path, output_path)
