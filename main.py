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

image = capture_q()

if image:
    image_data = encode(image)

    api = os.getenv('KEY')
    if not api:
        print("error, no api key")
    else:
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
                        {"type": "text", "text": "Recognize the question in the image, and provide a clear and short answer, provide just the answer to the question, nothing else."},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/png;base64,{image_data}"
                            }
                        }


                    ]
                }]
            }
        )

        if response.ok:        
            result = response.json()
            print(result["choices"][0]["message"]["content"])
        else:
            print(response.text)

else:
    print("no screenshot taken")


