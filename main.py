import os
import requests
import json
from fastapi import FastAPI
from models import ChatRequest
from dotenv import load_dotenv

# pip install fastapi
# pip install uvicorn
# pip install python-dotenv
# pip install requests


load_dotenv()

OPENROUTER_KEY = os.getenv("OPENROUTER_KEY")
OPENROUTER_URL = os.getenv("OPENROUTER_URL")
app = FastAPI(title='Ai Wrapper for openrouter api')


def call_openrouter_api(message: str):

    headers = {
            "Authorization": f"Bearer <{OPENROUTER_KEY}>",
            "Content-Type": "application/json",
        }
    body = {
            "model": "meta-llama/llama-3.3-70b-instruct:free",
            "messages": [
                {
                    "role": "user",
                    "content": message
                }
            ],

        }

    response = requests.post(url=OPENROUTER_URL, headers=headers, data=body)
    return response.json()


@app.post('/chat')
def chat(request: ChatRequest):
    pass
