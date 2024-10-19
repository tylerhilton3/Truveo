from main import submit
import openai
import os
from dotenv import load_dotenv
load_dotenv()

openai.api_key = str(os.getenv("openai_key"))

with open("prompt.txt", 'r') as file:
    prompt = file.read()

def summarize_text(text):
    response = openai.Client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content":
             f"{prompt}\n\n{text}"}
        ],
        max_tokens=200,  # Adjust the length of the summary
        temperature=0.5
    )
    
    # Extract the summary from the response
    summary = response.choices[0].message
    return summary

# Call the function to summarize the webpage text
summary = summarize_text(submit)
print(summary)




