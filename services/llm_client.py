import os
import json
import re
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("❌ Missing Gemini API Key in .env")

genai.configure(api_key=api_key)

MODEL_NAME = "gemini-2.0-flash"
model = genai.GenerativeModel(MODEL_NAME)


def clean_json(raw: str) -> dict:
    """Extract valid JSON from messy LLM output reliably."""
    try:
        # direct JSON
        return json.loads(raw)
    except:
        pass

    # Attempt to find JSON by locating the first '{' and matching braces.
    start = raw.find('{')
    if start == -1:
        raise ValueError("❌ Could not extract JSON: no opening brace found")

    depth = 0
    end = None
    for i in range(start, len(raw)):
        ch = raw[i]
        if ch == '{':
            depth += 1
        elif ch == '}':
            depth -= 1
            if depth == 0:
                end = i
                break

    if end is None:
        raise ValueError("❌ Could not extract JSON: no matching closing brace found")

    candidate = raw[start:end+1]
    try:
        return json.loads(candidate)
    except Exception as e:
        raise ValueError(f"❌ Could not parse extracted JSON: {e}\nRaw output:\n{raw}")


def evaluate_answer(question, answer, role, persona):
    prompt = f"""
    You are a highly strict interviewer evaluating a candidate for a {role} role.
    Persona style: {persona}

    Scoring must reflect quality:
    - Very strong real example, measurable impact → 9 or 10
    - Good but lacks depth or metrics → 6 or 7
    - Generic, short, or unclear → 4 or 5
    - Irrelevant, incorrect → 1 to 3

    DO NOT return explanations outside JSON.

    Return strictly in JSON format:
    {{
        "overall_score": number 1-10,
        "communication": number 1-10,
        "technical": number 1-10,
        "relevance": number 1-10,
        "topic": "{role}",
        "improvement": "Personalized feedback, 2-3 sentences"
    }}

    Question: {question}
    Answer: {answer}
    END JSON ONLY.
    """

    response = model.generate_content(prompt)
    raw = response.text.strip()

    try:
        return clean_json(raw)
    except Exception as e:
        print("⚠️ JSON Parsing Failed → fallback used:", e)
        # More varied fallback
        return {
            "overall_score": 5,
            "communication": 5,
            "technical": 4,
            "relevance": 5,
            "topic": role,
            "improvement": "You can provide more detailed reasoning and a real example to strengthen your answer."
        }
