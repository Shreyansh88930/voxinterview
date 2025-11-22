# core/state.py

import streamlit as st

def init_state():
    defaults = {
        "current_role": None,
        "experience_level": None,
        "persona": None,
        "interview_started": False,
        "interview_finished": False,
        "qa_pairs": [],
        "current_question": None,
        "current_topic": None,
        "chat_history": [],
        "overall_feedback": None,
        "max_questions": 6,  # Option B selected
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v


def add_chat_message(role: str, content: str):
    st.session_state.chat_history.append({"role": role, "content": content})


def add_qa_pair(question, answer, feedback, score, topic):
    st.session_state.qa_pairs.append(
        {
            "question": question,
            "answer": answer,
            "feedback": feedback,
            "score": score,
            "topic": topic,
        }
    )


def reset_interview():
    keys = [
        "interview_started",
        "interview_finished",
        "qa_pairs",
        "current_question",
        "current_topic",
        "chat_history",
        "overall_feedback",
    ]
    for k in keys:
        if k in ["qa_pairs", "chat_history"]:
            st.session_state[k] = []
        elif k in ["interview_started", "interview_finished"]:
            st.session_state[k] = False
        else:
            st.session_state[k] = None
