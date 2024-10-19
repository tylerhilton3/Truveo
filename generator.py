from scraper import full_content
import openai

openai.api_key = "key"

def summarize_text(text):
    response = openai.ChatCompletion.create(
        model="gpt-4",  # or "gpt-3.5-turbo" for GPT-3
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Please summarize the following text:\n\n{text}"}
        ],
        max_tokens=200,  # Adjust the length of the summary
        temperature=0.5
    )
    
    # Extract the summary from the response
    summary = response['choices'][0]['message']['content']
    return summary

# Call the function to summarize the webpage text
summary = summarize_text(webpage_text)
print(summary)