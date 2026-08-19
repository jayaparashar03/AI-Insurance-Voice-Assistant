import os
import tempfile
from datetime import datetime

from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient
from groq import Groq
import pyttsx3
import speech_recognition as sr
import gradio as gr

load_dotenv()

# ----------------------------
# Models
# ----------------------------

embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

qdrant = QdrantClient(
    url=os.getenv("QDRANT_URL"),
    api_key=os.getenv("QDRANT_API_KEY"),
    check_compatibility=False,
    timeout=60
)

groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))

MODEL = os.getenv("MODEL", "openai/gpt-oss-20b")

COLLECTION = "insurance_knowledge"
RELEVANCE_THRESHOLD = 0.35


# ----------------------------
# Save transcript
# ----------------------------

def save_transcript(question, answer):
    os.makedirs("transcripts", exist_ok=True)

    with open("transcripts/chat_log.txt", "a", encoding="utf-8") as f:
        f.write(f"\n[{datetime.now()}]\n")
        f.write(f"User: {question}\n")
        f.write(f"Bot: {answer}\n")

#-------------------------------
# save lead
#-------------------------------

def save_lead(name, phone):
    os.makedirs("leads", exist_ok=True)

    with open("leads/leads.csv", "a", encoding="utf-8") as f:
        f.write(f"{name},{phone}\n")

    return "Callback request submitted successfully."

# ----------------------------
# Suggested Questions
# ----------------------------

def suggested_questions():

    return """

---

### You can also ask

**Health Insurance**

- Tell me about Health Insurance
- Compare Health Insurance plans
- Which health plan is best for a family?

**Payments**

- Can I pay using UPI?
- Can I pay monthly?
- What payment methods are accepted?

**Claims**

- What documents are required?
- How long does claim approval take?

**Support**

- Can I renew my policy online?
- Connect me with a human advisor.
"""


# ----------------------------
# Voice Input
# ----------------------------

def speech_to_text(audio_path):
    if audio_path is None:
        return ""

    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_path) as source:
        audio = recognizer.record(source)

    try:
        return recognizer.recognize_google(audio)
    except Exception:
        return ""


# ----------------------------
# Voice Output
# ----------------------------

def text_to_speech(text):
    engine = pyttsx3.init()

    fd, path = tempfile.mkstemp(suffix=".mp3")
    os.close(fd)

    engine.save_to_file(text, path)
    engine.runAndWait()

    return path


# ----------------------------
# Chatbot
# ----------------------------

def ask_bot(question):

    if not question.strip():
        return "Please ask a question.", None

    vector = embedding_model.encode(question).tolist()

    results = qdrant.query_points(
        collection_name=COLLECTION,
        query=vector,
        limit=8
    ).points

    context_parts = []

    for r in results:
        if r.score >= RELEVANCE_THRESHOLD:
            text = r.payload.get("text", "")
            if text:
                context_parts.append(text)

    context = "\n\n".join(dict.fromkeys(context_parts))

    if not context.strip():

        answer = (
            "I don't have that information."
            + suggested_questions()
        )

        save_transcript(question, answer)

        audio = text_to_speech("I don't have that information.")

        return answer, audio

    prompt = f"""
You are Darwix Insurance's AI Voice Assistant.

Your role is to help customers understand insurance policies
and qualify potential leads.

Rules:

1. Answer ONLY from the retrieved context.
2. Never invent information.
3. If information is missing, reply exactly:
"I don't have that information."
4. Keep answers conversational.
5. Use headings and bullet points.
6. Do NOT create Markdown tables.
7. If the customer is interested in buying, renewing,
   comparing plans or requesting a quote,
   recommend the Request Callback tab.
8. If the customer requests a human,
   recommend the Request Callback tab.

Context:

{context}

Customer Question:

{question}
"""


    try:
        response = groq_client.chat.completions.create(
            model=MODEL,
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful insurance assistant."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.1
        )

        answer = response.choices[0].message.content.strip()

    except Exception:
        answer = "Sorry, I couldn't generate a response."

    extra = objection_response(question)
    if extra:
        answer += "\n\n" + extra
    escalation = human_escalation(question)
    if escalation:
        answer += "\n\n" + escalation
    answer += lead_hint(question)
    answer += suggested_questions()
    save_transcript(question, answer)
    audio = text_to_speech(answer.split("---")[0])
    return answer, audio


#---------------
# greeting
#---------------

def greeting_message():
    return (
        "Hello! Welcome to Darwix Insurance.\n\n"
        "I can help you understand Health, Life, Motor and Travel Insurance,"
        " compare plans, explain premiums, claims and policy renewal.\n\n"
        "How can I help you today?"
    )


def lead_hint(question):

    q = question.lower()

    keywords = [
        "buy", "purchase", "renew", "quote",
        "price", "premium", "compare",
        "advisor", "callback", "interested"
    ]

    if any(k in q for k in keywords):

        return (
            "\n\n### Next Step\n"
            "If you'd like personalised assistance, "
            "please open the **Request Callback** tab "
            "and share your name and phone number."
        )

    return ""


def objection_response(question):

    q = question.lower()

    if "expensive" in q or "costly" in q:
        return (
            "The Basic Health Plan is our affordable option with "
            "₹5 lakh coverage and an annual premium of ₹7,500."
        )

    if "later" in q:
        return (
            "No problem. You can explore the plans now and request "
            "a callback whenever you're ready."
        )

    if "not interested" in q:
        return (
            "That's completely fine. If you have questions later, "
            "I'll be happy to help."
        )

    return ""


def human_escalation(question):

    q = question.lower()

    words = [
        "human",
        "advisor",
        "agent",
        "representative",
        "person",
        "call me"
    ]

    if any(w in q for w in words):
        return (
            "Certainly. Please use the **Request Callback** tab "
            "and a Darwix Insurance advisor can contact you."
        )

    return ""

# ----------------------------
# Voice Chat
# ----------------------------

def voice_chat(audio):

    text = speech_to_text(audio)

    if not text:
        return "", "Couldn't understand the audio.", None

    answer, speech = ask_bot(text)

    return text, answer, speech

# ----------------------------
# UI
# ----------------------------

with gr.Blocks(title="Darwix Insurance Assistant") as demo:

    gr.Markdown("""
# 🏥 Darwix Insurance Voice Assistant

Welcome to Darwix Insurance.

### I can help with

- Health Insurance
- Life Insurance
- Motor Insurance
- Travel Insurance
- Premiums
- Claims
- Payment Methods
- Policy Renewal
- Waiting Periods

### How to use

1. Type your question or use Voice Chat.
2. Ask naturally.
3. I'll answer using the Darwix knowledge base.
4. If you're interested in a policy, I'll guide you to Request Callback.
5. If information isn't available, I'll clearly say:

**"I don't have that information."**
""")

    # ==================================
    # TEXT CHAT
    # ==================================

    with gr.Tab("Text Chat"):

        text_input = gr.Textbox(
            label="Ask your question",
            placeholder="Example: Tell me about Health Insurance"
        )

        text_answer = gr.Markdown(label="Answer")

        speech_output = gr.Audio(
            label="Voice Response",
            autoplay=False
        )

        with gr.Row():
            ask_btn = gr.Button("Ask")
            clear_btn = gr.Button("Clear")

        ask_btn.click(
            ask_bot,
            inputs=text_input,
            outputs=[text_answer, speech_output]
        )

        # ENTER key support
        text_input.submit(
            ask_bot,
            inputs=text_input,
            outputs=[text_answer, speech_output]
        )

        # Clear
        clear_btn.click(
            lambda: ("", "", None),
            outputs=[text_input, text_answer, speech_output]
        )

        gr.Examples(
            examples=[
                "Tell me about Health Insurance",
                "Compare Health Insurance plans",
                "Tell me about Life Insurance",
                "Explain Motor Insurance",
                "What Travel Insurance plans are available?",
                "What is the Basic Health Plan premium?",
                "Can I pay using UPI?",
                "How long does claim approval take?"
            ],
            inputs=text_input
        )

    # ==================================
    # VOICE CHAT
    # ==================================

    with gr.Tab("Voice Chat"):

        audio_input = gr.Audio(
            sources=["microphone"],
            type="filepath",
            label="Speak your question"
        )

        recognized_text = gr.Textbox(
            label="Recognized Speech"
        )

        voice_answer = gr.Markdown(
            label="Answer"
        )

        voice_output = gr.Audio(
            label="Voice Reply",
            autoplay=False
        )

        voice_btn = gr.Button("Ask with Voice")

        voice_btn.click(
            voice_chat,
            inputs=audio_input,
            outputs=[
                recognized_text,
                voice_answer,
                voice_output
            ]
        )

    # ==================================
    # CALLBACK REQUEST
    # ==================================

    with gr.Tab("📞 Request Callback"):

        name_input = gr.Textbox(
            label="Your Name"
        )

        phone_input = gr.Textbox(
            label="Phone Number"
        )

        status_output = gr.Textbox(
            label="Status"
        )

        submit_btn = gr.Button(
            "Request Callback"
        )

        submit_btn.click(
            save_lead,
            inputs=[name_input, phone_input],
            outputs=status_output
        )

demo.launch(
    share=False
)