📌 README.md — VoxInterview 🚀

AI-Powered Smart Interview Practice Assistant

VoxInterview is an interactive AI interviewer built using Streamlit + Gemini Flash API, designed to help users practice job interviews through a conversational chat experience. It dynamically generates follow-up questions based on the user’s answers and evaluates responses with a detailed scoring rubric.

🎯 Key Features
Feature	Description
🔁 Fully Conversational Interview Flow	AI asks questions, evaluates your answer, then asks the next one automatically
🧠 Adaptive Questioning	Follows-up based on your previous response & selected job role
🎤 Voice Input	Answer using speech-to-text (Web Speech API in browser)
🔊 AI Voice for Questions	Browser reads questions aloud using speech synthesis
📊 Performance Summary	Scoring breakdown, strengths, weaknesses, recommended topics
⚡ Real-Time Response Scoring	Dynamic scoring powered by Gemini-2.0 Flash
💾 State Management	Maintains chat history & feedback in session
🛠️ Tech Stack
Component	Technology
Frontend UI	Streamlit
AI LLM	Google Gemini 2.0 Flash
Voice Recognition	Browser SpeechRecognition API
Styling	Custom CSS (Glassmorphism UI)
State & Evaluation Logic	Python
📂 Project Structure
📁 voxinterview/
├── app.py  # Main Streamlit App
├── core/
│   ├── state.py
├── agents/
│   ├── interview_agent.py  # Dynamic Q Generation
│   ├── feedback_agent.py   # AI Scoring & Summary
├── services/
│   ├── llm_client.py       # Gemini API communication
│   ├── text_to_speech.py   # Browser Speech Recognition support
├── ui/
│   ├── layout.py           # Sidebar + CSS injection
├── .env                    # API key stored securely
├── .gitignore              # Ensures key not pushed to GitHub
└── README.md

🔐 API Key Setup

1️⃣ Create .env file in project root:

GEMINI_API_KEY=your_api_key_here


2️⃣ .env is already included in .gitignore
✔ This ensures your API key is NOT uploaded to GitHub.

The demo repository will mention that “API key can be found locally in .env (ignored in GitHub for security).”

▶️ How to Run
1️⃣ Install Dependencies
pip install -r requirements.txt

2️⃣ Start Application
streamlit run app.py


✔ App opens at → http://localhost:8501

🧪 Roles Supported

✔ Software Engineer
✔ Data Analyst
✔ Sales Roles
✔ Generic Behavioral Interviews

Easily customizable inside agents/interview_agent.py

📌 Future Enhancements

Resume upload for personalized questions

Video interview analysis (eye contact & tone)

Login + Candidate history tracking

Export full report as PDF

Author

Shreyansh Palwalia
B.Tech — Delhi Technological University
📧 shreyanshpalwalia_se22a12_72@dtu.ac.in