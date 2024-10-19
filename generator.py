import openai
import os
from dotenv import load_dotenv

def initialize_key():
    load_dotenv()

    # Load the API key from the environment
    openai.api_key = os.getenv("OPENAI_API_KEY")

    if not openai.api_key:
        raise ValueError("API Key not found. Make sure it's set in your environment variables.")

def prompt(text):
    initialize_key()
    with open("megaprompt.txt", "r") as file:
        prompt = file.read()
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content":
             f"{prompt}\n\n{text}"}
        ],
        max_tokens = 500,  # Adjust the length of the summary
        temperature = 0
    )
    return response.choices[0].message.content

def get_summary(text):
    return prompt("", text)

def get_ytquery(text):
    return prompt("", text)

def get_articlevid(text):
    return prompt("", text)
