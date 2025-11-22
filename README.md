<h1 align="center">🤖 VoxInterview – AI Interview Practice Partner</h1>

<p align="center">
A Conversational AI Agent that conducts real-time adaptive mock interviews with dynamic scoring and voice interaction.
<br>
Built for the <b>Eightfold.ai Agentic AI Assignment</b>
</p>

---

## 📌 About The Project

VoxInterview is an **AI-powered Interview Practice Partner** that simulates real interview environments through natural conversational flow.

The agent:
- Asks questions based on **role**, **persona**, and **your previous answers**
- Evaluates responses with **intelligent scoring**
- Provides **personalized improvement feedback**
- Generates complete **performance summary**
- Supports **voice answering** & **AI voice output**
- Handles multiple **user personas** and behaviors

This ensures a **human-like interview experience** with continuous adaptation.

---

## ✨ Key Features

| Feature | Benefit |
|--------|---------|
| Adaptive questioning | AI asks follow-ups based on previous answer + skills |
| Role-based difficulty progression | Evaluates relevant competencies |
| Persona-driven interviewer styles | Friendly, Strict, Analytical, etc. |
| Voice Input 🎙 | Speak answers (browser speech recognition) |
| AI Voice Output 🔊 | Questions spoken using Web Speech API |
| Dynamic Scoring | Evaluation across clarity, technical depth, structure |
| Personalized Feedback | Clear improvement suggestions every turn |
| Interview Summary | Strengths + Weaknesses + Suggested learning plan |

---

## 🔍 Architecture Overview

voxinterview/
│
├─ app.py # Streamlit app and UI logic
│
├─ agents/
│ ├─ interview_agent.py # Agentic next-question generation
│ └─ feedback_agent.py # AI-based scoring & summary
│
├─ services/
│ ├─ llm_client.py # Gemini LLM API logic
│ ├─ speech_to_text.py # (Optional) Local STT helper
│ └─ text_to_speech.py # Browser-based TTS integration
│
├─ core/
│ └─ state.py # Session state manager
│
├─ ui/
│ └─ layout.py # Styling, sidebar and glass UI
│
├─ .env.example # Environment variables template
├─ requirements.txt # Python dependencies
└─ README.md # Project documentation


---

## 🎮 Demo Workflow

| User Style | System Behavior |
|-----------|----------------|
| Confused User | Guiding follow-up questions |
| Efficient User | Short, targeted conversation |
| Off-topic User | Penalizes relevance score |
| Chatty User | Keeps flow structured |

🎥 **Demo video will be attached on final submission**

---

## 🎯 Assignment Requirements Mapping

| Requirement | How it’s fulfilled |
|------------|------------------|
| Conversational quality | Memory-aware chat with natural flow |
| Agentic behavior | Fully autonomous question generation |
| Technical decisioning | Modular AI-driven pipeline |
| Intelligence | LLM scoring + dynamic feedback |
| Adaptability | Personas + interview style variations |
| Multiple user personas handled | YES (all 4 tested) |

---

## 🔐 API Keys Setup

Create a `.env` file (based on included `.env.example`):

```bash
GEMINI_API_KEY=YOUR_KEY_HERE


⚠ Do NOT commit your .env file
(Already protected in .gitignore)

⚙️ Installation & Run
# 1️⃣ Clone repo
git clone https://github.com/<your-username>/voxinterview.git
cd voxinterview

# 2️⃣ Create environment
python -m venv venv
venv/Scripts/activate    # Windows
# OR
source venv/bin/activate # Mac/Linux

# 3️⃣ Install dependencies
pip install -r requirements.txt

# 4️⃣ Run App 🚀
streamlit run app.py


App opens automatically at:
👉 http://localhost:8501/

🧠 AI Evaluation Metrics

Each answer evaluated on:

Metric	Weight
Communication	✔
Technical Depth	✔
Relevance	✔
Structure / STAR Framework	✔
Persona-based behavior	✔

Follow-up questions target improving weak areas.