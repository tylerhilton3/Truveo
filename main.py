import tkinter as tk
from tkinter import messagebox
import validators
from scraper import get_text


# Create the root window
root = tk.Tk()
root.geometry("400x200")
root.title("I-Hack 2024")

# Create a label for the title at the top
title_label = tk.Label(root, text="Curecancer.py", font=("Helvetica", 16, "bold"))
title_label.pack(pady=10)

# Create an entry box with a placeholder
entry = tk.Entry(root, width=50, fg='gray')
entry.insert(0, "Enter a link you would like to fact check:")
entry.pack(pady=10)

# Function to clear the placeholder when typing
def on_click(event):
    if entry.get() == "Enter a link you would like to fact check:":
        entry.delete(0, "end")  # delete all the text in the entry
        entry.config(fg='black')

# Function to restore the placeholder if the entry is empty
def on_focus_out(event):
    if entry.get() == "":
        entry.insert(0, "Enter a link you would like to fact check:")
        entry.config(fg='gray')

# Bind the functions to the entry widget
entry.bind("<FocusIn>", on_click)
entry.bind("<FocusOut>", on_focus_out)

# Function to handle the input and process the link
def submit():
    user_input = entry.get()
    # Validate the URL using the validators library
    if validators.url(user_input):
        print("Link submitted:", user_input)
        # Clear the entry box and refill with placeholder text
        entry.delete(0, "end")
        entry.insert(0, "Enter a link you would like to fact check:")
        entry.config(fg='gray')
        text_data = get_text(user_input)
        print(text_data)
    else:
        # Show a pop-up message for invalid link
        messagebox.showerror("Invalid URL", "Please enter a valid URL starting with 'https://' or 'http://'.")
    
# Create a button to submit the input
submit_button = tk.Button(root, text="Submit", command=submit, font=("Helvetica", 12))
submit_button.pack(pady=20)

# Run the application
root.mainloop()
