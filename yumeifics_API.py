import requests
import time
from dotenv import load_dotenv
from urllib.parse import urlparse
import os
load_dotenv()

YUMEFICS_API_KEY = os.getenv("YUMEFICS_API_KEY")
COMFYUI_URL = os.getenv("YUMEFICS_WEB")
_parsed = urlparse(COMFYUI_URL)
YUMEIFICS_BASE_URL = f"{_parsed.scheme}://{_parsed.netloc}"

def generate_sample(config: dict, variants: list[str] | None = None ) -> dict:
    response = requests.post(
        COMFYUI_URL,
        headers={
            "Authorization": "Bearer "+YUMEFICS_API_KEY, 
            "Content-Type": "application/json"
        },
        json=config
        
    )
    return response.json()

def poll_sample(pollUrl):
    while True:
        status_res=requests.get(
            YUMEIFICS_BASE_URL + pollUrl,
            headers={
                "Authorization": "Bearer "+YUMEFICS_API_KEY
            }
        )
        status = status_res.json()
        if status["status"] == "complete":
            return status["chapter"]
        else:
            time.sleep(5)