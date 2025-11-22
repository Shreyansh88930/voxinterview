# services/llm_client.py

import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# Load Gemini API Key
api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("❌ Missing Gemini API Key in .env")

# Configure Gemini API
genai.configure(api_key=api_key)

# Model used for both question generation & evaluation
MODEL_NAME = "gemini-2.0-flash"
model = genai.GenerativeModel(MODEL_NAME)


def extract_json(text: str) -> dict:
    """Extract valid JSON from model output string."""
    text = text.strip()

    # If response already looks like JSON
    if text.startswith("{") and text.endswith("}"):
        return json.loads(text)

    # If wrapped in code blocks like ```json {..} ```
    if "```" in text:
        cleaned = text.replace("```json", "").replace("```", "").strip()
        return json.loads(cleaned)

    raise ValueError("Invalid JSON Output from LLM:\n" + text)


def evaluate_answer(question, answer, role, persona):
    prompt = f"""
    You are a strict expert interviewer evaluating a candidate for a {role} position.
    Persona style: {persona}

    CRITICAL SCORING RULES (MANDATORY):
    - If answer is < 4 lines OR generic → score <= 5
    - If no specific example, STAR structure, or measurable impact → score <= 6
    - If strong justification, clarity, deep reasoning → score >= 8
    - If unrelated or incorrect → score <= 3
    - Avoid giving 7 unless performance is clearly average

    Rate the answer on:
    1. Communication clarity
    2. Technical depth (if applicable)
    3. Relevance to the question
    4. Structure and completeness

    Output MUST be CLEAN JSON ONLY:
    {{
        "overall_score": integer 1-10,
        "communication": integer 1-10,
        "technical": integer 1-10,
        "relevance": integer 1-10,
        "topic": "topic category",
        "improvement": "Specific and personalized improvement feedback (2-3 sentences)"
    }}

    Question: {question}
    Answer: {answer}
    """

    response = model.generate_content(prompt)
    raw = response.text.strip()

    try:
        return extract_json(raw)
    except Exception:
        cleaned = raw.replace("```json", "").replace("```", "").strip()
        return extract_json(cleaned)
