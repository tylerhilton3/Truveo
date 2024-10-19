from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

# Function to add captions to the video
def add_captions(video_file, script, output_file="final_video.mp4"):
    # Load the video
    video_clip = VideoFileClip(video_file)

    # Generate text clips for each caption in the script
    text_clips = []
    for line in script:
        caption = TextClip(
            line["text"],
            fontsize=24,
            color='white',
            size=(video_clip.w, 50),
            method='caption'
        ).set_position(('center', video_clip.h - 100)).set_duration(line["end_time"] - line["start_time"]).set_start(line["start_time"])
        
        text_clips.append(caption)

    # Composite the video with the captions
    final_video = CompositeVideoClip([video_clip, *text_clips])

    # Write the result to a file
    final_video.write_videofile(output_file, codec="libx264")
    print(f"Final video saved as {output_file}")

# Example usage
if __name__ == "__main__":
    # Example script
    script = [
        {
            "text": "Welcome to the wonders of nature. In this video, we will explore the beauty of natural landscapes.",
            "start_time": 0,
            "end_time": 10
        },
        {
            "text": "The vast forests and flowing rivers offer serenity and peace to all who witness them.",
            "start_time": 11,
            "end_time": 20
        },
        {
            "text": "Nature is a reminder of the power and beauty that surrounds us.",
            "start_time": 21,
            "end_time": 30
        }
    ]

    # Add captions to the video
    add_captions("background_video.mp4", script, "final_video_with_captions.mp4")
