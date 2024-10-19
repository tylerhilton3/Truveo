import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import validators
import scraper as scr
import prompter as pr
import youtubehandler as yth
import voiceoverhandler as voh
import os
import json
from moviepy.editor import VideoFileClip, concatenate_videoclips, AudioFileClip, concatenate_audioclips
def delete():
    files = [
    "outputs/yt1.mp4",
    "outputs/yt2.mp4",
    "outputs/yt3.mp4",
    "outputs/yt4.mp4",
    "outputs/voice1.mp3",
    "outputs/voice2.mp3",
    "outputs/voice3.mp3",
    "outputs/voice4.mp3",
    "outputs/voice5.mp3",
    "outputs/voice6.mp3",
    "final_video.mp4"
    ]
    for file in files:
        try:
            os.remove(file)
        except FileNotFoundError:
            pass


### UI Implementation
delete()
root = tk.Tk()
root.geometry("400x200")
root.title("Truveo")
icon = tk.PhotoImage(file='images/logo.png')
root.iconphoto(False, icon)

title_label = tk.Label(root, text="Article Credibility Checker", font=("Helvetica", 16, "bold"))
title_label.pack(pady=10)

entry = tk.Entry(root, width=50, fg='gray')
entry.pack(pady=10)

def on_click(event):
    if entry.get() == "Enter a link you would like to fact check:":
        entry.delete(0, "end")
        entry.config(fg='black')

def on_focus_out(event):
    if entry.get() == "":
        entry.insert(0, "Enter a link you would like to fact check:")
        entry.config(fg='gray')

entry.bind("<FocusIn>", on_click)
entry.bind("<FocusOut>", on_focus_out)

def submit():
    user_input = entry.get()
    if validators.url(user_input):
        entry.delete(0, "end")
        entry.insert(0, "Enter a link you would like to fact check:")
        entry.config(fg='gray')
        save_file()
        data = json.loads(pr.prompt(scr.get_text(user_input)))
        with open("structure.json", "w") as x:
            json.dump(data, x)
        
        yth.get_videos()
        voh.get_voiceovers()
        create_video()
        root.quit()
    else:
        messagebox.showerror("Invalid URL", "Please enter a valid URL starting with 'https://' or 'http://'.")

OUTPUT_PATH = "final_video.mp4"
def save_file():
    global OUTPUT_PATH
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    
    # Open a file dialog for saving
    file_path = filedialog.asksaveasfilename(defaultextension=".mp4", 
                                             filetypes=[("MP4 Video files", "*.mp4"), 
                                                        ("All Files", "*.*")],
                                             title="Save your video as...")
    if file_path:
        print(f"Your video will be saved to: {file_path}")
        OUTPUT_PATH = file_path


def create_video():
    width = 1920
    height = 1080
    yt_video_one = VideoFileClip("outputs/yt1.mp4")
    yt_video_two = VideoFileClip("outputs/yt2.mp4")
    yt_video_three = VideoFileClip("outputs/yt3.mp4")
    yt_video_four = VideoFileClip("outputs/yt4.mp4")
    yt_video_one = yt_video_one.resize(newsize=(width, height)).set_fps(60)
    yt_video_two = yt_video_two.resize(newsize=(width, height)).set_fps(60)
    yt_video_three = yt_video_three.resize(newsize=(width, height)).set_fps(60)
    yt_video_four = yt_video_four.resize(newsize=(width, height)).set_fps(60)
    audio_one = AudioFileClip("outputs/voice1.mp3")
    audio_two = AudioFileClip("outputs/voice2.mp3")
    audio_three = AudioFileClip("outputs/voice3.mp3")
    audio_four = AudioFileClip("outputs/voice4.mp3")
    audio_five = AudioFileClip("outputs/voice5.mp3")
    audio_six = AudioFileClip("outputs/voice6.mp3")
    audio_one_duration = audio_one.duration
    audio_two_duration = audio_two.duration
    audio_three_duration = audio_three.duration
    audio_four_duration = audio_four.duration
    audio_five_duration = audio_five.duration
    audio_six_duration = audio_six.duration
    combined_audio = concatenate_audioclips([audio_one, audio_two, audio_three, audio_four, audio_five, audio_six])
    subclip_one = yt_video_one.subclip(0,audio_one_duration)
    subclip_two = yt_video_two.subclip(0,audio_two_duration)
    subclip_three = yt_video_three.subclip(0,audio_three_duration)
    subclip_four = yt_video_four.subclip(0,audio_four_duration+audio_five_duration+audio_six_duration)
    combined_clips = concatenate_videoclips([subclip_one, subclip_two, subclip_three, subclip_four])
    final_clip = combined_clips.set_audio(combined_audio)
    final_clip.write_videofile(OUTPUT_PATH, fps=60)
    

# Create a button to submit the input
submit_button = tk.Button(root, text="Submit", command=submit, font=("Helvetica", 12))
submit_button.pack(pady=20)

# Run the application
root.mainloop()

