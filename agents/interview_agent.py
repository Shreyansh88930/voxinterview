# agents/interview_agent.py

import json
from services.llm_client import model


def _topics_for_role(role: str):
    role = (role or "").lower()
    if "data" in role:
        return ["Behavioral", "SQL", "Analytics", "Case Study"]
    if "sales" in role:
        return ["Behavioral", "Customer Handling", "Pitching", "Closing Deals"]
    return ["Behavioral", "Coding / DSA", "System Design", "Teamwork"]


def get_next_question(state):
    role = state.current_role or "Software Engineer"
    persona = state.persona or "Neutral"
    qa_pairs = state.qa_pairs
    asked = len(qa_pairs)
    max_q = state.max_questions

    if asked >= max_q:
        state.interview_finished = True
        return None

    topics = _topics_for_role(role)
    topic_idx = min(asked, len(topics) - 1)
    topic = topics[topic_idx]

    difficulty = "easy" if asked == 0 else ("hard" if asked > 2 else "medium")

    last_answer = qa_pairs[-1]["answer"] if asked > 0 else "N/A"

    prompt = f"""
    You are an interviewer for a {role} role.
    Persona: {persona}

    Topic for the next question: {topic}
    Difficulty: {difficulty}

    Candidate's last answer: {last_answer}

    Ask EXACTLY one interview question.
    No greetings, no comments, only the question.
    """

    try:
        resp = model.generate_content(prompt)
        q = resp.text.strip()
    except:
        q = "Okay, can you explain more about your experience?"

    state.current_topic = topic
    return q

from services.llm_client import evaluate_answer

def evaluate_single_answer(question, answer, role, persona):
    return evaluate_answer(question, answer, role, persona)


def summarize_full_interview(qa_pairs, role, persona):
    transcript = ""

    for i, qa in enumerate(qa_pairs, start=1):
        transcript += f"Q{i}: {qa['question']}\nA{i}: {qa['answer']}\nScore:{qa['score']}\n\n"

    prompt = f"""
    Provide a SHARP INTERVIEW SUMMARY for a {role} role.
    Candidate Persona Feedback Style: {persona}

    Return strict JSON structure:
    {{
        "summary": "3-4 sentence objective summary",
        "strengths": ["distinct bullet strengths"],
        "areas_to_improve": ["clear improvement areas"],
        "suggested_topics": ["skills to revise"]
    }}

    Transcript:
    {transcript}
    """

    response = model.generate_content(prompt)
    raw = response.text.strip()

    try:
        return json.loads(raw)
    except:
        cleaned = raw.split("```json")[-1].split("```")[0]
        return json.loads(cleaned)
