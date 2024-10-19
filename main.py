# import tkinter as tk
# from tkinter import messagebox
# from tkinter import filedialog
# import validators
# from scraper import get_text
# from prompter import prompt
from video_search import search_video, download_video  # Import functions for video search and download
from ai_voiceover import generate_ai_voiceover  # Import function for AI voiceover
from add_captions import add_captions_with_timing  # Import function for adding captions
import os
#import json

### UI Implementation
# root = tk.Tk()
# root.geometry("400x200")
# root.title("Truveo")
# icon = tk.PhotoImage(file='images/logo.png')
# root.iconphoto(False, icon)

# title_label = tk.Label(root, text="Curecancer.py", font=("Helvetica", 16, "bold"))
# title_label.pack(pady=10)

# entry = tk.Entry(root, width=50, fg='gray')
# entry.insert(0, "Enter a link you would like to fact check:")
# entry.pack(pady=10)

# def on_click(event):
#     if entry.get() == "Enter a link you would like to fact check:":
#         entry.delete(0, "end")
#         entry.config(fg='black')

# def on_focus_out(event):
#     if entry.get() == "":
#         entry.insert(0, "Enter a link you would like to fact check:")
#         entry.config(fg='gray')

# entry.bind("<FocusIn>", on_click)
# entry.bind("<FocusOut>", on_focus_out)

def process_video():
    download_folder = "\outputs"
    json_path = "script.json"  # Set your JSON path here

    # Ensure the download folder exists
    os.makedirs(download_folder, exist_ok=True)

    # Search for the video
    video_id, title = search_video("1 minute meme video")

    if video_id:
        # Download the video
        download_video(video_id, download_folder)

        # Generate the AI voiceover
        ai_voiceover_path = generate_ai_voiceover(json_path)

        # Add captions (you can adjust this function to accept ai_voiceover_path if needed)
        #add_captions(download_folder, ai_voiceover_path)


if __name__ == "__main__":
    # Replace this with actual user input handling if necessary
    user_input = "1 minute meme"  # Placeholder for user input
    process_video()

# Function to handle the input and process the link
# def submit():
#     user_input = entry.get()
#     if validators.url(user_input):
#         entry.delete(0, "end")
#         entry.insert(0, "Enter a link you would like to fact check:")
#         entry.config(fg='gray')
#         save_file()

#         data = prompt(get_text(user_input))
#         print(data)
#         data = json.loads(data)
#         print(data)
#         filepath = "outputs/structure.json"

#         with open(filepath, 'w') as json_file:
#             json.dump(data, json_file)
#     else:
#         messagebox.showerror("Invalid URL", "Please enter a valid URL starting with 'https://' or 'http://'.")

# def save_file():
#     root = tk.Tk()
#     root.withdraw()  # Hide the main window
    
#     # Open a file dialog for saving
#     file_path = filedialog.asksaveasfilename(defaultextension=".mp4", 
#                                              filetypes=[("MP4 Video files", "*.mp4"), 
#                                                         ("All Files", "*.*")],
#                                              title="Save your video as...")
#     if file_path:
#         print(f"Your video will be saved to: {file_path}")
# # Create a button to submit the input
# submit_button = tk.Button(root, text="Submit", command=submit, font=("Helvetica", 12))
# submit_button.pack(pady=20)

# # Run the application
# root.mainloop()
