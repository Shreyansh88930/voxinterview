# app.py

import streamlit as st
import json
from streamlit.components.v1 import html

from core.state import init_state, add_chat_message, add_qa_pair
from ui.layout import inject_css, sidebar_controls, header
from agents.interview_agent import get_next_question
from agents.feedback_agent import evaluate_single_answer, summarize_full_interview
from services.text_to_speech import recognition_script


def main():
    st.set_page_config(
        page_title="VoxInterview – AI Interview Practice Partner",
        page_icon="🤖",
        layout="wide"
    )

    inject_css()
    init_state()
    header()

    # ensure recording flag exists
    if 'recording' not in st.session_state:
        st.session_state['recording'] = False

    role, level, persona, use_voice = sidebar_controls()
    st.session_state.current_role = role
    st.session_state.persona = persona

    # Clear answer box before widget render if flagged
    if st.session_state.get("clear_answer", False):
        st.session_state["answer_box"] = ""
        st.session_state["clear_answer"] = False

    col_main, col_summary = st.columns([3, 2])

    # ================= MAIN CHAT PANEL =================
    with col_main:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)

        if not st.session_state.interview_started:
            st.info("👈 Configure settings & click **Start Interview** to begin.")
            st.markdown("</div>", unsafe_allow_html=True)
            return

        if not st.session_state.current_question and not st.session_state.interview_finished:
            q = get_next_question(st.session_state)
            st.session_state.current_question = q
            add_chat_message("assistant", q)

        st.subheader("Interview Chat")

        for msg in st.session_state.chat_history:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

        # If still interviewing…
        if not st.session_state.interview_finished and st.session_state.current_question:

            # Speak Question Button
            if st.button("🔊 Hear AI Voice Question"):
                q_js = json.dumps(st.session_state.current_question or "")
                html(f"""
                    <script>
                        (function(){{
                            const text = {q_js};
                            const msg = new SpeechSynthesisUtterance(text);
                            msg.lang = "en-US";
                            msg.pitch = 1;
                            msg.rate = 1;
                            window.speechSynthesis.cancel();
                            window.speechSynthesis.speak(msg);
                        }})();
                    </script>
                """, height=0)

            # Voice input button
            if use_voice and st.button("🎙 Speak Answer"):
                # mark recording active so we can show a Stop button
                st.session_state['recording'] = True
                html(recognition_script(), height=0)
                # Some Streamlit builds may not expose experimental_rerun.
                rerun = getattr(st, "experimental_rerun", None)
                if callable(rerun):
                    rerun()


            # Show stop button when recording is active
            if st.session_state.get('recording'):
                stop_clicked = st.button("⏹ Stop Recording")
                if stop_clicked:
                    st.session_state['recording'] = False
                    html("""
                        <script>
                            try {
                                if(window._voxRecStop){ window._voxRecStop(); }
                                else if(window._voxRec){ window._voxRec.stop(); }
                            } catch(e){ console.warn('stop script error', e); }
                        </script>
                    """, height=0)
                    rerun = getattr(st, "experimental_rerun", None)
                    if callable(rerun):
                        rerun()
                # Do NOT clear st.session_state["answer_box"] here!

            # Answer text-field
            answer = st.text_area(
                "Your Answer",
                key="answer_box",
                placeholder="Speak or type your answer...",
                height=140
            )

            submit_col, finish_col = st.columns([1, 1])
            submit = submit_col.button("Submit Answer ✅")
            finish_now = finish_col.button("Finish Interview 🏁")

            if submit and answer and answer.strip():
                add_chat_message("user", answer)
                question = st.session_state.current_question
                with st.spinner("Evaluating your answer..."):
                    result = evaluate_single_answer(question, answer, role, persona)
                score = result.get("overall_score", "?")
                feedback = result.get("improvement") or "Try adding more structure and real examples."
                topic = result.get("topic") or st.session_state.get("current_topic", "General")
                # Emoji based on performance
                rating_emoji = "🔥" if score >= 8 else ("🆗" if score >= 6 else "⚠️")
                add_qa_pair(question, answer, feedback, score, topic)
                add_chat_message(
                    "assistant",
                    f"{rating_emoji} **Score: {score}/10**\n\n🧩 {feedback}\n\n📌 *Topic: {topic}*"
                )
                # Next question logic
                if len(st.session_state.qa_pairs) >= st.session_state.max_questions:
                    st.session_state.interview_finished = True
                    st.session_state.current_question = None
                else:
                    next_q = get_next_question(st.session_state)
                    st.session_state.current_question = next_q
                    add_chat_message("assistant", next_q)
                # Set flag to clear input on next rerun
                st.session_state["clear_answer"] = True
                rerun = getattr(st, "experimental_rerun", None)
                if callable(rerun):
                    rerun()

            if finish_now:
                st.session_state.interview_finished = True
                st.session_state.current_question = None
                st.rerun()

        else:
            st.success("🎯 Interview Completed! See Performance →")

        st.markdown("</div>", unsafe_allow_html=True)

    # ================= SUMMARY PANEL =================
    with col_summary:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.subheader("📊 Performance Summary")

        st.metric("Questions Answered", len(st.session_state.qa_pairs))

        if st.session_state.interview_finished and st.session_state.qa_pairs:
            if st.session_state.overall_feedback is None:
                with st.spinner("Generating your interview report…"):
                    st.session_state.overall_feedback = summarize_full_interview(
                        st.session_state.qa_pairs, role, persona
                    )

            report = st.session_state.overall_feedback

            st.write(report.get("summary", ""))
            st.write("---")

            if report.get("strengths"):
                st.write("💪 Strengths:")
                for s in report["strengths"]:
                    st.write(f"- {s}")

            if report.get("areas_to_improve"):
                st.write("⚠ Areas to Improve:")
                for a in report["areas_to_improve"]:
                    st.write(f"- {a}")

            if report.get("suggested_topics"):
                st.write("📚 Suggested Topics:")
                for t in report["suggested_topics"]:
                    st.write(f"- {t}")

        st.markdown("</div>", unsafe_allow_html=True)


if __name__ == "__main__":
    main()
