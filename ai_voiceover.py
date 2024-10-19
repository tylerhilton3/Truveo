from gtts import gTTS
import json
import os

def generate_ai_voiceover(json_path):
    # Load the script from the JSON file
    with open(json_path, 'r') as f:
        script = json.load(f)

    # Create a list to store the lines to be spoken
    lines_to_read = []
    
    # Assuming script[0][i][0] are the lines to read
    for i in range(2):  # Loop through the first three script lines
        lines_to_read.append(script[0][i][0])
        
    # Split the credibility rating into three parts
    credibility_lines = script[0][3]  # script[1][1] is assumed to be a list of credibility statements
    for line in credibility_lines:
        lines_to_read.append(line)  # Append each part of the credibility statement

    # Join the lines into a single text
    full_text = " ".join(lines_to_read)

    # Generate the AI voiceover
    tts = gTTS(text=full_text, lang='en')
    voiceover_path = "ai_voiceover.mp3"  # Specify the path for the voiceover file
    tts.save(voiceover_path)
    
    return voiceover_path

# Example usage
if __name__ == "__main__":
    json_path = "script.json"  # Replace with the path to your JSON file
    ai_voiceover_path = generate_ai_voiceover(json_path)
    print(f"AI voiceover saved to: {ai_voiceover_path}")
