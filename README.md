# Darwix Insurance Voice Assistant

## Overview

Darwix Insurance Voice Assistant is a Retrieval-Augmented Generation (RAG) chatbot built using Groq, Qdrant Cloud and Gradio. It answers customer queries using only the provided insurance knowledge base.

## Features

- RAG chatbot using Qdrant Cloud
- Voice-to-Text
- Text-to-Speech
- Conversation flow
- Lead qualification
- Human escalation
- Request Callback form
- Transcript logging

## Technologies Used

- Python
- Gradio
- Groq API
- Qdrant Cloud
- Sentence Transformers
- SpeechRecognition
- pyttsx3

## Folder Structure

```text
Darwix_AI_Assessment/
├── app.py
├── ingest.py
├── requirements.txt
├── README.md
├── .env.example
├── data/
│   └── insurance.md
├── leads/
│   └── leads.csv
├── recordings/
├── transcripts/
│   └── chat_log.txt
```

## Installation

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file using `.env.example`.

## Run

```bash
python ingest.py
python app.py
```

## Example Questions

- Tell me about Health Insurance
- Compare Health Insurance plans
- Can I pay using UPI?
- What documents are required for a claim?
- Connect me with a human advisor