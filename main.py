import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import validators
import scraper as scr
import prompter as pr
import youtubehandler as yth
import voiceoverhandler as voh
import add_captions as ac
import os
import json

### UI Implementation
root = tk.Tk()
root.geometry("400x200")
root.title("Truveo")
icon = tk.PhotoImage(file='images/logo.png')
root.iconphoto(False, icon)

title_label = tk.Label(root, text="Curecancer.py", font=("Helvetica", 16, "bold"))
title_label.pack(pady=10)

entry = tk.Entry(root, width=50, fg='gray')
entry.insert(0, "Enter a link you would like to fact check:")
entry.pack(pady=10)

def on_click():
    if entry.get() == "Enter a link you would like to fact check:":
        entry.delete(0, "end")
        entry.config(fg='black')

def on_focus_out():
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

        data = pr.prompt(scr.get_text(user_input))
        data = json.loads(data)
        filepath = "structure.json"

        with open(filepath, 'w') as json_file:
            json.dump(data, json_file)
    else:
        messagebox.showerror("Invalid URL", "Please enter a valid URL starting with 'https://' or 'http://'.")

def save_file():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    
    # Open a file dialog for saving
    file_path = filedialog.asksaveasfilename(defaultextension=".mp4", 
                                             filetypes=[("MP4 Video files", "*.mp4"), 
                                                        ("All Files", "*.*")],
                                             title="Save your video as...")
    if file_path:
        print(f"Your video will be saved to: {file_path}")
# Create a button to submit the input
submit_button = tk.Button(root, text="Submit", command=submit, font=("Helvetica", 12))
submit_button.pack(pady=20)

# Run the application
root.mainloop()
