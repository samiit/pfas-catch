"""Audio utilities for handling audio processing and transcription."""

import os
import openai
from dotenv import load_dotenv

load_dotenv()

open_ai_key = os.getenv("open_ai_key")


def get_text_from_whisper(audio_buffer: bytes) -> str:
    response = openai.Audio.transcribe(
        "whisper-1", file=audio_buffer, api_key=open_ai_key
    )
    return response["text"]
