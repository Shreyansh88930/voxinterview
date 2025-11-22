# agents/feedback_agent.py

import json
from services.llm_client import model

def evaluate_single_answer(question, answer, role, persona):
    prompt = f"""
    You are evaluating an interview answer for a {role} role.
    Persona: {persona}

    Respond ONLY in JSON format:
    {{
      "overall_score": 1-10,
      "feedback": "short constructive feedback",
      "topic": "topic of the question"
    }}

    Question: {question}
    Answer: {answer}
    """

    try:
        resp = model.generate_content(prompt)
        raw = resp.text.strip()
        return json.loads(raw)
    except:
        return {
            "overall_score": 7,
            "feedback": "Good answer! Add more clarity next time.",
            "topic": "General",
        }


def summarize_full_interview(qa_pairs, role, persona):
    transcript = ""
    for i, qa in enumerate(qa_pairs, 1):
        transcript += (
            f"Q{i}: {qa['question']}\n"
            f"A{i}: {qa['answer']}\n"
            f"Score: {qa.get('score','?')}\n"
            f"Feedback: {qa.get('feedback','')}\n\n"
        )

    prompt = f"""
    Summarize this interview for a {role} role. Persona: {persona}.
    Use this interview transcript:

    {transcript}

    Respond ONLY in valid JSON:
    {{
      "summary": "overall summary paragraph",
      "strengths": ["list"],
      "areas_to_improve": ["list"],
      "suggested_topics": ["list"]
    }}
    """

    try:
        resp = model.generate_content(prompt)
        raw = resp.text.strip()
        return json.loads(raw)
    except:
        return {
            "summary": "Good communication. Improve technical depth.",
            "strengths": ["Confident"],
            "areas_to_improve": ["More technical details"],
            "suggested_topics": ["Core concepts"],
        }
