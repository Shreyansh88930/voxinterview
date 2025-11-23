# agents/feedback_agent.py

from services.llm_client import evaluate_answer
from agents.interview_agent import summarize_full_interview as _summarize_interview


def evaluate_single_answer(question: str, answer: str, role: str, persona: str) -> dict:
    """Wrapper to LLM answer evaluation."""
    return evaluate_answer(question, answer, role, persona)


def summarize_full_interview(qa_pairs, role: str, persona: str) -> dict:
    """Wrapper to summarization logic from interview_agent."""
    return _summarize_interview(qa_pairs, role, persona)
