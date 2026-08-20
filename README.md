# Darwix Insurance Voice Assistant

# Darwix Insurance AI Assistant DEMO VIDEO

[Watch the Demo Video]
FOR Q1:
https://drive.google.com/file/d/1YOaWPMATPa9FImCyZa_N4KGBCtuynz1c/view?usp=sharing
FOR Q2(using q1):
https://drive.google.com/file/d/1z_6oma2_ekCpLdRDeWoceBA5_VuBvn0N/view?usp=sharing

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


# Q2 (using q1)
## Question 2 — Production-Ready Knowledge Base

The insurance knowledge base was extended into a structured and traceable
retrieval system for the voice assistant.

The knowledge records include:

- Record ID
- Title
- Content
- Category
- Source
- Version
- PII flag
- Chunk ID

The source data is cleaned and divided into logical sections before being
embedded using `all-MiniLM-L6-v2` and indexed in Qdrant.

The retrieval pipeline uses semantic similarity to find relevant insurance
information. Retrieved records retain their source and metadata so that the
information used by the assistant can be traced back to the source document.

Five retrieval queries were tested covering:

- Product information
- Policy information
- Claims
- Payment methods
- Human support

All five tests returned a relevant top-ranked record.

The Q2 implementation and evaluation are available in:

```text
q2/
├── knowledge_base_schema.md
├── data_cleaning.md
├── retrieval_test.py
├── retrieval_tests.md
└── q2_report.md


# Question 3 – Native-Language Voice Bot Prototype

## Objective

The objective of Question 3 is to design localized conversational voice-bot prototypes for two different markets:

1. Philippines (Insurance Domain)
2. Indonesia (Consumer Finance Domain)

The focus is on language adaptation, code-switching, local terminology, and culturally appropriate customer interactions.

---

## Markets Covered

### Philippines

Supported Languages:

- English
- Filipino
- Taglish (English + Filipino)

Example Customer Queries:

- Magkano ang premium?
- Pwede bang monthly ang payment?
- What is a beneficiary?

Localization Features:

- Insurance terminology support
- Natural Filipino conversational style
- Taglish code-switching handling
- Human-assistance escalation support

---

### Indonesia

Supported Languages:

- Bahasa Indonesia

Example Customer Queries:

- Berapa DP?
- Berapa tenor pinjaman?
- Saya belum bisa bayar cicilan.

Localization Features:

- Consumer-finance terminology support
- Natural Indonesian conversational responses
- Finance-specific vocabulary recognition
- Human-assistance escalation support

---

## Code-Switching Support

The prototype supports mixed-language customer conversations.

Examples:

Philippines:

Customer:
> Magkano ang premium?

Customer:
> Pwede bang monthly payment?

Indonesia:

Customer:
> Berapa DP untuk financing ini?

The bot preserves commonly used local financial and insurance terms instead of forcing complete translation.

---

## Localization Approach

The implementation includes:

- Language-specific response templates
- Local insurance terminology
- Local finance terminology
- Cultural adaptation for customer communication
- Human-agent escalation responses
- Safe handling of unsupported requests

The bot avoids generating unsupported promises related to approvals, pricing, discounts, or policy benefits.

---

## Project Structure

```text
q3/
│
├── bot.py
├── test_q3.py
├── q3_report.md
│
├── philippines/
│   ├── knowledge.md
│   └── test_cases.md
│
└── indonesia/
    ├── knowledge.md
    └── test_cases.md
```

---

## Testing

Testing was performed using localized customer scenarios.

### Philippines Test Scenarios

- Premium inquiry
- Beneficiary inquiry
- Coverage inquiry
- Monthly payment inquiry
- Human-agent request
- Policy clarification
- Appreciation response
- Unsupported promise request

### Indonesia Test Scenarios

- Tenor inquiry
- Down-payment inquiry
- Installment inquiry
- Payment schedule inquiry
- Human-agent request
- Eligibility inquiry
- Appreciation response
- Unsupported discount request

---

## Running the Prototype

Navigate to the Q3 folder:

```bash
cd q3
```

Run the test suite:

```bash
python test_q3.py
```

The output displays localized responses for both markets.

---

## Example Output

Philippines:

Customer:
> Magkano ang premium?

Bot:
> Ang premium ay depende sa plan at eligibility. Maaaring tulungan ka ng representative sa quote.

Indonesia:

Customer:
> Berapa tenor pinjaman?

Bot:
> Tenor tergantung produk pembiayaan yang dipilih.

---

## Limitations

Current implementation:

- Rule-based language detection
- Prototype conversational flows
- No live telephony integration
- No production speech recognition
- No CRM integration

A production deployment would require larger multilingual datasets, advanced language identification, speech processing, and integration with enterprise systems.

---

## Deliverables

Included files:

- bot.py
- test_q3.py
- q3_report.md
- Philippines knowledge base
- Indonesia knowledge base
- Localized test cases
- Screenshots demonstrating execution
