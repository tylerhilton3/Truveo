import tkinter as tk
from tkinter import messagebox
import validators
from scraper import get_text
from generator import get_summary


### UI Implementation
root = tk.Tk()
root.geometry("400x200")
root.title("Truveo")

title_label = tk.Label(root, text="Curecancer.py", font=("Helvetica", 16, "bold"))
title_label.pack(pady=10)

entry = tk.Entry(root, width=50, fg='gray')
entry.insert(0, "Enter a link you would like to fact check:")
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



# Function to handle the input and process the link
def submit():
    user_input = entry.get()
    if validators.url(user_input):
        entry.delete(0, "end")
        entry.insert(0, "Enter a link you would like to fact check:")
        entry.config(fg='gray')
        print(get_summary(get_text(user_input)))
    else:
        messagebox.showerror("Invalid URL", "Please enter a valid URL starting with 'https://' or 'http://'.")
    
# Create a button to submit the input
submit_button = tk.Button(root, text="Submit", command=submit, font=("Helvetica", 12))
submit_button.pack(pady=20)

# Run the application
root.mainloop()
