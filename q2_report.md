# Q2 — Production-Ready Knowledge Base

## Overview

The knowledge base was extended to make the insurance information structured,
searchable, and traceable for the RAG pipeline used by the Darwix Insurance
Assistant.

## Source Data

The current source document is:

```text
data/insurance.md
```

It contains insurance product and policy information covering health, life,
motor, travel, claims, payments, renewal, eligibility, waiting periods and
customer support.

## Data Preparation

The source content is divided into logical sections before indexing.

The preparation process considers:

- Empty sections
- Duplicate information
- Repeated content
- Inconsistent terminology
- Irrelevant content
- Accidental PII

Customer lead information is kept separate from the knowledge base.

## Knowledge Record Structure

Each indexed record contains:

- `record_id`
- `title`
- `content`
- `category`
- `source`
- `version`
- `pii`
- `chunk_id`

This metadata allows retrieved information to be traced back to its source.

## Taxonomy

The knowledge base uses categories including:

- Health Insurance
- Life Insurance
- Motor Insurance
- Travel Insurance
- Coverage
- Eligibility
- Waiting Period
- Claims
- Premium Payment Methods
- Cashless Hospitals
- Policy Renewal
- Human Support

## Embedding and Indexing

Knowledge chunks are converted into embeddings using:

```text
all-MiniLM-L6-v2
```

The vectors are stored in Qdrant using cosine similarity.

The same embedding model is used for user queries.

## Retrieval

The retrieval pipeline is:

```text
User Question
      ↓
Embedding
      ↓
Qdrant Similarity Search
      ↓
Relevance Filtering
      ↓
Relevant Knowledge
      ↓
Groq LLM
      ↓
Grounded Answer
```

The application uses a relevance threshold before passing retrieved content
to the language model.

## Source Traceability

Retrieved records contain source metadata including:

- Record ID
- Title
- Category
- Source
- Version
- Chunk ID

The application now displays the source document used for a retrieved answer.

The current source is:

```text
data/insurance.md
```

## Retrieval Evaluation

Five retrieval queries were tested.

### 1. Basic Health Plan Premium

**Query**

> What is the Basic Health Plan premium?

**Retrieved record**

`health_insurance_basic_health_plan_1`

**Result**

The Basic Health Plan record was the top result and contained the requested
premium information.

**Verdict:** Correct

### 2. Pre-existing Disease Waiting Period

**Query**

> What is the waiting period for pre-existing diseases?

**Retrieved record**

`health_insurance_waiting_period_12`

**Result**

The Waiting Period record was the top result and contained the relevant
waiting-period information.

**Verdict:** Correct

### 3. Claim Documents

**Query**

> What documents are required for a claim?

**Retrieved record**

`claims_required_claim_documents_14`

**Result**

The Required Claim Documents record was the top result and contained the
relevant claim-document information.

**Verdict:** Correct

### 4. UPI Payment

**Query**

> Can I pay my premium using UPI?

**Retrieved record**

`premium_payment_methods_premium_payment_methods_15`

**Result**

The Premium Payment Methods record was the top result and contained the
relevant UPI payment information.

**Verdict:** Correct

### 5. Human Advisor

**Query**

> I want to speak with a human insurance advisor.

**Retrieved record**

`human_support_human_support_18`

**Result**

The Human Support record was the top result and matched the customer's request
for human assistance.

**Verdict:** Correct

## Q1 Integration

The Q2 knowledge base is connected to the Question 1 assistant.

The application retrieves relevant records from Qdrant before generating the
answer.

The retrieved source is also exposed in the assistant response for
traceability.

## Unsupported Questions

The assistant was tested with an unrelated question:

> What is the capital of France?

The system correctly returned:

> "I don't have that information."

This prevents unrelated information from being presented as insurance
knowledge.

## Limitations

The current knowledge base is based on the supplied insurance source material.

The current implementation uses a single source document and a relatively
small retrieval test set.

A production implementation would require a larger and continuously maintained
knowledge corpus, automated data-quality checks, stronger retrieval evaluation,
knowledge version management, and additional security controls.

## Conclusion

The Q2 implementation adds structured metadata, source tracking, categorization,
versioning, vector indexing, retrieval evaluation, and traceability to the
insurance knowledge base.

The resulting knowledge base is used by the Q1 insurance assistant for
grounded responses.