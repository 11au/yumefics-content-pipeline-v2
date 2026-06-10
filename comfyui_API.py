import json
import requests
from dotenv import load_dotenv
import os

load_dotenv()

COMFYUI_URL = os.getenv("COMFYUI_URL");

def generateImage(prompt):
    with open("Workflow_api.json", "r") as f:
        workflow = f.json()
    
    workflow["3"]["inputs"]["text"] = prompt

    updated_json=json.dump(workflow)

    image_response=requests.post(
        COMFYUI_URL+"/prompt",
        json=updated_json
    )

    if "error" in image_response:
        return ({"error": image_response["error"]})
    else: 
        return image_response["prompt_id"]

def poll_image_response(image_response): 
    while True: 
        if "error" in image_response:
            return image_response
        else: 
            image = requests.get(
               COMFYUI_URL+"/history/"+image_response
            )
            return image
