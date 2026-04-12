from PIL import Image
import subprocess
import os
import requests
import base64

def capture_q():
    question = "screenshot.png"
    subprocess.run(["screencapture", "-i", question])
    if os.path.exists(question):
        return question
    else:
        print("cancelled operation")

def encode(image):
    with open(image, "rb") as file:
        return base64.b64encode(file.read()).decode('utf-8')


def speak(text):
    subprocess.run([
        "python", "-m", "f5_tts_mlx.generate",
        "--ref-audio", "voice.wav",
        "--ref-text", "Hey, miss, I'm getting the answers forty two. No, wait, forty five",
        "--text", text,
        "--method", "midpoint",
        "--q", "4",
        "--output", "result.wav"
    ])

    subprocess.run(["afplay", "result.wav"], check=False)
    return "playing audio before saying it in zoom"

image = capture_q()

def ask_ai(image):
    api = os.getenv('KEY')
    if not api:
        return None, 'no api key found.'
    response = requests.post(
            "https://ai.hackclub.com/proxy/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {api}",
                "Content-Type": "application/json"
            },
            json={
                "model": "google/gemini-3-flash-preview",
                "messages": [{
                    "role": "user",
                    "content": [
                        {"type": "text", "text": "Recognize the question in the image, and provide a clear and short answer, provide just the answer to the question, if the answer is in numbers, please provide the numbers as words, eg: 4 will become four, dont use roman numerals like 'i', provide them as 'one', provide a comma after the roman numeral, and dont use dashes, please provide a comma after each answer, dont use brackets, and questions with variables, please add a space after the number and its respective variable. nothing else."},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/png;base64,{image}"
                            }
                        }


                    ]
                }]
            }
        )
    if response.ok:
        return response.json()["choices"][0]["message"]["content"].strip(), None
    return None, response.text


