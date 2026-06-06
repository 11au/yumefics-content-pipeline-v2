import requests
import time
from dotenv import load_dotenv
import os
load_dotenv()

YUMEFICS_API_KEY = os.getenv("YUMEFICS_API_KEY")
COMFYUI_URL = os.getenv("COMFYUI_URL")

def generate_sample(fandomSlug, characterSlug, toneConfig):
    response = requests.post(
        COMFYUI_URL,
        headers={
            "Authorization": "Bearer"+YUMEFICS_API_KEY, 
            "Content-Type": "application/json"
        },
        json={
            "fandomSlug": fandomSlug,
            "characterSlug": characterSlug,
            "config":toneConfig
        }
    )
    return response.json()

def poll_sample(pollUrl):
    while True:
        status_res=requests.get(
            pollUrl,
            headers={
                "Authorization": "Bearer"+YUMEFICS_API_KEY
            }
        )
        status = status_res.json()
        if status == "complete":
            return status["chapter"]
        else:
            time.sleep(1)