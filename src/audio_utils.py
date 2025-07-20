"""Audio utilities for handling audio processing and transcription."""

import asyncio
import os

from openai import AsyncOpenAI
from openai.helpers import LocalAudioPlayer
from dotenv import load_dotenv

openai = AsyncOpenAI()

load_dotenv()

open_ai_key = os.getenv("open_ai_key")


openai = AsyncOpenAI(api_key=open_ai_key)


async def text_to_speech(input_text: str) -> None:
    async with openai.audio.speech.with_streaming_response.create(
        model="gpt-4o-mini-tts",
        voice="coral",
        input=input_text,
        instructions="Speak in a cheerful and positive tone.",
        response_format="pcm",
    ) as response:
        await LocalAudioPlayer().play(response)
