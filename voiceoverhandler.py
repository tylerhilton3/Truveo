from gtts import gTTS
import json
import os

def get_voiceovers():
    with open(("structure.json"), 'r') as x:
        structure = json.load(x)

    lines_to_read = {
        "summary1":     structure[0][0][0],
        "summary2":     structure[0][1][0],
        "summary3":     structure[0][2][0],
        "cred1":        structure[1][0][0],
        "cred2":        structure[1][0][1],
        "cred score":   structure[1][0][2]
        }
    
    voice = 1
    for line in lines_to_read.values():
        print(line)
        tts = gTTS(text=line, lang='en', slow=False)
        directory = "outputs/"
        file_name = f"voice{voice}.mp3"
        voiceover_path = os.path.join(directory, file_name)
        tts.save(voiceover_path)
        voice += 1

get_voiceovers()