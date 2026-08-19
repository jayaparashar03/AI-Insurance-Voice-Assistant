# Darwix Insurance Voice Assistant

# Darwix Insurance AI Assistant DEMO VIDEO

[Watch the Demo Video]
FOR Q1:
https://drive.google.com/file/d/1YOaWPMATPa9FImCyZa_N4KGBCtuynz1c/view?usp=sharing
FOR Q2:


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


An AI-powered insurance assistant built for the Darwix AI Engineer Assessment.

The application uses a retrieval-augmented generation (RAG) approach to answer insurance-related questions from a knowledge base. It also supports voice interaction and a callback flow for customers who want human assistance.

## Features

- Insurance question answering using a knowledge base
- Semantic search with Qdrant
- Sentence Transformer embeddings
- Groq LLM for response generation
- Text chat using Gradio
- Voice input and speech recognition
- Text-to-speech responses
- Fallback for unsupported questions
- Human assistance / callback flow
- Lead storage
- Conversation logging

## How it works

The user can type or speak a question. For a voice query, the speech is first converted into text.

The question is converted into an embedding and searched against the insurance knowledge stored in Qdrant. Relevant information is then provided to the LLM to generate the response.

If the required information is not available, the assistant responds:

> "I don't have that information."

Customers who want human assistance can use the Request Callback section.

## Knowledge Base

The current knowledge base is:

```text
data/insurance.md
```

It contains information about insurance plans, coverage, premiums, claims, payment methods, renewal, eligibility and waiting periods.

## Project Structure

```text
app.py
ingest.py
requirements.txt
README.md
.env.example
.gitignore

data/
    insurance.md

leads/
    leads.csv

recordings/
    recording1.m4a
    recording2.m4a
    recording3.m4a

transcripts/
    transcript1.txt
    transcript2.txt
    transcript3.txt
    chat_log.txt
```

## Running the project

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a local `.env` file with:

```text
QDRANT_URL=
QDRANT_API_KEY=
GROQ_API_KEY=
MODEL=
```

Run the knowledge-base ingestion:

```bash
python ingest.py
```

Start the application:

```bash
python app.py
```

The Gradio interface will be available at the local URL shown in the terminal.

## Example questions

- Tell me about Health Insurance
- Compare Health Insurance plans
- What is the Basic Health Plan premium?
- Can I pay using UPI?
- What documents are required for a claim?
- How long does claim approval take?
- Can I renew my policy online?
- Connect me with a human advisor.

## Test recordings and transcripts

Three test conversations are included in the `recordings` folder with their corresponding transcripts in the `transcripts` folder.

The conversations cover different customer interaction scenarios.

## Callback and conversation logs

Callback details are stored in:

```text
leads/leads.csv
```

Conversation logs are stored in:

```text
transcripts/chat_log.txt
```

Only test data should be used in these files.

## Limitations

This is an assessment prototype. The current version uses a web interface rather than a production telephony system and stores callback information locally.

For production use, the system would need secure data storage, CRM integration, authentication, monitoring, stronger PII protection and production voice/telephony integration.

## Security

API keys and other credentials must not be committed to the repository.

The `.env.example` file is provided as a template. The actual `.env` file should remain local.


# Q2
## Question 2 — Production-Ready Knowledge Base

The knowledge base was extended with structured metadata and source
traceability for retrieval.

Each knowledge record includes a record ID, title, category, source, version,
PII flag and chunk ID.

The knowledge base is embedded using `all-MiniLM-L6-v2` and indexed in Qdrant
using cosine similarity.

Five retrieval queries were evaluated across product, policy, claims, payment
and human-support scenarios. The five tests returned relevant top-ranked
records.

The Q2 implementation and evaluation are documented in:

```text
q2/
├── knowledge_base_schema.md
├── data_cleaning.md
├── retrieval_test.py
├── retrieval_tests.md
└── q2_report.md
