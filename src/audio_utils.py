"""Audio utilities for handling audio processing and transcription."""

import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

open_ai_key = os.getenv("open_ai_key")

client = OpenAI(api_key=open_ai_key)


def get_text_from_whisper(audio_buffer: bytes) -> str:
    response = client.audio.transcriptions.create(model="whisper-1", file=audio_buffer)
    return response["text"]
