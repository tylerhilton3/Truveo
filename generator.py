from openai import OpenAI
client = OpenAI()
import os
from dotenv import load_dotenv
load_dotenv()

client.api_key = str(os.getenv("openai_key"))

with open("prompt.txt", 'r') as file:
    prompt = file.read()

def test(text):
    response = client.chat.completions.create(
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



