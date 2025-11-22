# ui/layout.py

import streamlit as st
from core.config import ROLES, PERSONAS


def inject_css():
    with open("ui/styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def sidebar_controls():
    st.sidebar.title("⚙️ Interview Setup")

    role = st.sidebar.selectbox("Role", list(ROLES.keys()))
    level = st.sidebar.selectbox("Experience Level", ROLES[role]["levels"])
    persona = st.sidebar.selectbox("Interviewer Persona", list(PERSONAS.keys()))

    st.sidebar.write("---")
    use_voice = st.sidebar.checkbox("Enable voice answer via audio upload", value=True)

    if st.sidebar.button("Start / Restart Interview"):
        from core.state import reset_interview
        reset_interview()
        st.session_state.current_role = role
        st.session_state.experience_level = level
        st.session_state.persona = persona
        st.session_state.interview_started = True
        st.session_state.interview_finished = False

    return role, level, persona, use_voice


def header():
    st.markdown(
        """
        <div class="glass-card">
            <h1>🧠 VoxInterview</h1>
            <p style="opacity:0.8;">
            An AI-powered mock interview partner with adaptive questions, voice answers, and futuristic UI.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.write("")
