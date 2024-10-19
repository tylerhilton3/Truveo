import pyttsx3

def generate_voiceover(script_text, output_path):
    engine = pyttsx3.init()
    engine.save_to_file(script_text, output_path)
    engine.runAndWait()

if __name__ == "__main__":
    script_path = r"C:\path\to\your\script.txt"  # Path to your script text file
    output_path = r"C:\Users\14064\OneDrive\Documents\school\2024Fall\Ihack\IntegrityAndMight-1\videos\voiceover.mp3"

    with open(script_path, 'r') as f:
        script_text = f.read()

    generate_voiceover(script_text, output_path)
