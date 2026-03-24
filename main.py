from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from emotion_detector import detect_emotion
from messages import get_message, get_resources

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class TextInput(BaseModel):
    text: str

@app.post("/analyze")
def analyze(input: TextInput):
    emotion = detect_emotion(input.text)
    return {
        "emotion": emotion,
        "message": get_message(emotion),
        "resources": get_resources(emotion),
    }