# services/speech_to_text.py

import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

# Load Gemini API Key
api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("❌ Missing GEMINI_API_KEY or GOOGLE_API_KEY in .env file!")

genai.configure(api_key=api_key)


def transcribe_audio(file) -> str:
    """
    Audio-to-text using Google Gemini Speech (Audio-to-Text)
    Currently supports wav/mp3 uploads from Streamlit.
    """
    try:
        audio_data = file.read()
        audio_filename = file.name

        response = genai.upload_to_gemini(
            name=audio_filename,
            data=audio_data,
            mime_type="audio/wav" if audio_filename.endswith(".wav") else "audio/mpeg"
        )

        # Generate transcription request
        model = genai.GenerativeModel("gemini-2.0-flash")
        result = model.generate_content(
            [
                response,
                "Transcribe the audio to clean text. Return only transcription."
            ]
        )
        
        return result.text.strip()

    except Exception as e:
        print("Gemini STT Error:", e)
        return "[Transcription failed — please try again or type your answer]"
