import requests
import json
from dotenv import load_dotenv
import os
load_dotenv()

OPENROUTER_API_KEY=os.getenv("CHAPTER_KEY")


# API call function 
def filter_chapter(chapter: str):
    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": "Bearer "+OPENROUTER_API_KEY,
            "Content-Type": "application/json",
        },
        data=json.dumps({
            "model": "openai/gpt-oss-120b: free",
            "messages": [
                {
                    "role": "user",
                    "content": "meow"
                }
            ]
        })

    )