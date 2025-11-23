# services/text_to_speech.py

def speak_text(text: str) -> str:
    """
    Browser will handle speech.
    Just return text as-is.
    """
    return text


def recognition_script() -> str:
    """Stable speech-to-text for Streamlit.
    - Keeps transcript in text area
    - Updates Streamlit session state
    - NO auto rerun until submit
    """
    return """
    <script>
        (function(){
            const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
            if (!SpeechRecognition) {
                alert("Speech Recognition not supported in this browser.");
                return;
            }

            const rec = new SpeechRecognition();
            rec.lang = "en-US";
            rec.interimResults = true;
            rec.continuous = true;

            let finalTranscript = "";

            rec.onresult = (event) => {
                let interim = "";
                for (let i = event.resultIndex; i < event.results.length; i++) {
                    const result = event.results[i];
                    if (result.isFinal) {
                        finalTranscript += result[0].transcript;
                    } else {
                        interim += result[0].transcript;
                    }
                }

                const transcript = (finalTranscript + interim).trim();

                // 🔥 Official & stable session update event
                const evt = new CustomEvent("streamlit:setSessionState", {
                    detail: { answer_box: transcript }
                });
                try { window.parent.document.dispatchEvent(evt); } catch(e) { /* ignore */ }

                // Update UI textarea
                try {
                    const parentDoc = window.parent.document;
                    // try to match Streamlit's textarea by id or placeholder
                    let textarea = parentDoc.querySelector("textarea[id^='answer_box']");
                    if(!textarea){
                        textarea = parentDoc.querySelector("textarea[placeholder='Speak or type your answer...']");
                    }
                    if(!textarea){
                        const all = parentDoc.querySelectorAll('textarea');
                        textarea = all.length ? all[0] : null;
                    }

                    if (textarea) {
                        const nativeSetter = Object.getOwnPropertyDescriptor(window.HTMLTextAreaElement.prototype, 'value')?.set;
                        if(nativeSetter){ nativeSetter.call(textarea, transcript); }
                        else { textarea.value = transcript; }

                        textarea.dispatchEvent(new Event('input', { bubbles: true }));
                        textarea.dispatchEvent(new Event('change', { bubbles: true }));
                        try{ textarea.selectionStart = textarea.selectionEnd = textarea.value.length; } catch(e){}
                    }
                } catch(e){ console.warn('[speech-recognition] ui update failed', e); }
            };

            rec.onerror = (err) => console.error("STT error:", err);

            rec.onend = () => {
                if (!window._stopRecording) {
                    rec.start(); // auto-restart only while in Mic mode
                }
            };

            // Global stop flag
            window._stopRecording = false;
            window.stopSTT = function() {
                window._stopRecording = true;
                try{ rec.stop(); } catch(e){}
            };

            // Backwards compatibility for older handlers
            window._voxRecStop = window.stopSTT;
            window._voxRecShouldStop = function(){ return window._stopRecording; };

            rec.start();
        })();
    </script>
    """
