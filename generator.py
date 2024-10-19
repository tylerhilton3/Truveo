import openai
import os
from dotenv import load_dotenv

def initialize_key():
    load_dotenv()

    # Load the API key from the environment
    openai.api_key = os.getenv("OPENAI_API_KEY")

    if not openai.api_key:
        raise ValueError("API Key not found. Make sure it's set in your environment variables.")


def get_summary(text):
    initialize_key()
    with open("testprompt.txt", "r") as file:
        prompt = file.read()
    response = openai.chat.completions.create(
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
    summary = response.choices[0].message.content
    return summary

def get_ytquery():
    pass

def get_articlevid():
    pass

