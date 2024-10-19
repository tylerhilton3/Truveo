import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Load the API key from the environment
openai.api_key = os.getenv("OPENAI_API_KEY")

if not openai.api_key:
    raise ValueError("API Key not found. Make sure it's set in your environment variables.")


with open("prompt.txt", "r") as file:
    prompt = file.read()
response = openai.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Say hi to my friend caleb"}
    ],
    max_tokens=200,  # Adjust the length of the summary
    temperature=0.5
)
print(response.choices[0].message.content)