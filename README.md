# 🤖 VoxInterview — AI Interview Practice Assistant

VoxInterview is an **AI-powered interactive interview simulator** built using **Streamlit + Google Gemini**, designed to help candidates practice technical and behavioral interviews through real conversation flow like ChatGPT.

It asks follow-up questions, evaluates your responses, scores performance, and recommends improvements — just like a real interviewer! 🎤🧠🚀

---

## ✨ Key Features

| Feature | Description |
|--------|-------------|
| 🔁 Continuous Interview Flow | Ask → Answer → Get Score → Next Question Automatically |
| 🧠 Adaptive Questioning | Next question depends on your previous response & role |
| 🎤 Voice Input | Speak your answers (Web SpeechRecognition API) |
| 🔊 AI Voice Output | Questions spoken aloud using Speech Synthesis |
| 📊 AI Evaluation | Scores clarity, technical depth, relevance & structure |
| 💬 Chat History | Full conversation saved on screen |
| 📝 Final Interview Report | Strengths, weaknesses, suggested improvement areas |

---

## 🧱 Architecture Overview

### 🔹 High-Level Architecture

User (Text/Voice Input)
|
V
Streamlit UI (Frontend)
|
V
Agents Layer
────────────────────────
| interview_agent.py | → Generates next question using Gemini
| feedback_agent.py | → Scores + evaluates answers
────────────────────────
|
V
Gemini 2.0 Flash API (LLM)
|
V
Structured JSON Feedback (Score + Analysis)
|
V
UI Display + Performance Summary


### 🔹 Component Breakdown

| Layer | Responsibility |
|-------|----------------|
| UI Layer | Voice/Text Input, chat rendering, sidebar settings |
| State Management | Uses Streamlit Session State for Q&A memory |
| Interview Agent | Role-based question generation & context |
| Evaluation Agent | AI performance scoring & actionable feedback |
| Gemini Model | NLP → understanding + scoring |
| Local Browser APIs | Speech recognition & Text-to-speech |

---

## 🛠️ Tech Stack

| Category | Technology |
|---------|------------|
| Frontend UI | Streamlit |
| AI/LLM Engine | Google Gemini 2.0 Flash |
| Voice Recognition | Web SpeechRecognition API (Client-side) |
| Text-to-Speech | SpeechSynthesis (Browser-based) |
| Backend Logic | Python |
| Styling | Custom CSS (Glassmorphism) |

---

## 📂 Folder Structure

📦 voxinterview/
├── app.py # Streamlit UI + Interview flow handling
├── core/
│ ├── state.py # Shared state (history, answers, scores)
├── agents/
│ ├── interview_agent.py # Question generator
│ ├── feedback_agent.py # Scoring engine & summary
├── services/
│ ├── llm_client.py # Gemini API wrapper (dynamic JSON parsing)
│ ├── text_to_speech.py # Voice recognition support
├── ui/
│ ├── layout.py # Sidebar + UI styling
├── .env # Gemini API key (secret - ignored in GitHub)
├── .gitignore # Prevents API key from leaking 🚫
└── README.md


---

## 🔐 API Key Configuration

Create `.env` file in project root:

```env
GEMINI_API_KEY=your_api_key_here


✔ .env already added to .gitignore
✔ The API key will NOT be committed to GitHub
➡️ Evaluation team can request the key if needed

▶️ Run the Application

Install dependencies:

pip install -r requirements.txt


Launch:

streamlit run app.py


App starts at → http://localhost:8501

🎯 Roles Supported

Software Engineering (DSA + System Design + Behavioral)

Data Analyst (SQL + Case + Behavioral)

Sales (Customer handling + Pitching)

Generic Behavioral Interviews

Easy to extend for other domains 🧩

🚀 Future Enhancements
Planned Add-on	Benefit
Resume Upload	Personalized interview questions
Video Answer Input	Evaluate confidence, body language
PDF Report Download	Easy sharing with mentors/recruiters
User Login	Track improvement history
👨‍💻 Developer Info

Built by Shreyansh Palwalia
B.Tech — Delhi Technological University (DTU), India 🇮🇳

📧 Email: shreyanshpalwalia_se22a12_72@dtu.ac.in

🌐 GitHub: Shreyansh88930
