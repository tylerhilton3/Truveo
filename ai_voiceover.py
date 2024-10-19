import json
from gtts import gTTS

# Load the script from the JSON file
def load_script(json_file):
    with open(json_file, 'r') as f:
        script_data = json.load(f)
    return script_data['script']

# Generate AI voiceover for each line in the script
def generate_voiceover(script, output_audio_file="voiceover.mp3"):
    full_text = " ".join([line["text"] for line in script])
    
    # Use gTTS (Google Text-to-Speech) to generate the audio
    tts = gTTS(text=full_text, lang='en')
    tts.save(output_audio_file)
    print(f"Voiceover saved as {output_audio_file}")

# Example usage
if __name__ == "__main__":
    script = load_script("script.json")
    generate_voiceover(script, "voiceover.mp3")
