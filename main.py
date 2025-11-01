import os
import requests
import json
from fastapi import FastAPI
from models import ChatRequest, ChatResponse
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware



# pip install fastapi
# pip install uvicorn
# pip install python-dotenv
# pip install requests


load_dotenv()

OPENROUTER_KEY = os.getenv("OPENROUTER_KEY")
OPENROUTER_URL = os.getenv("OPENROUTER_URL")
app = FastAPI(title='Ai Wrapper for openrouter api')
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # හෝ ["http://localhost:5173"]
    allow_credentials=True,
    allow_methods=["*"],  # POST, OPTIONS, GET හැමදෙයක්ම allow කරනවා
    allow_headers=["*"],
)

def call_openrouter_api(message: str):
    headers = {
        "Authorization": f"Bearer {OPENROUTER_KEY}",
        "Content-Type": "application/json",
    }
    body = {
        "model": "meta-llama/llama-3.3-70b-instruct:free",
        "messages": [
            {
                "role": "system",
                "content": "You are an Helpful AI Assistant ,"
                           "Who gives travel recommendations,"
                           "on eco-friendly places in sri Lanka ,"
                           ""

            },
            {
                "role": "user",
                "content": message
            }
        ]
    }

    response = requests.post(url=OPENROUTER_URL, headers=headers, json=body)
    return response.json()['choices'][0]['message']['content']




@app.post('/chat')
def chat(request: ChatRequest):
    return call_openrouter_api(request.message)
