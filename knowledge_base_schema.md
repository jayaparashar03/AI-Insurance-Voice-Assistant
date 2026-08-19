# Knowledge Base Schema

## Purpose

The knowledge base is designed to store insurance information in a structured, searchable, and traceable format.

The knowledge base will be used by the retrieval system and connected to the voice assistant.

## Record Schema

Each knowledge-base record contains the following fields:

| Field | Description |
|---|---|
| `record_id` | Unique identifier for the knowledge record |
| `title` | Name of the product, policy, process, or topic |
| `content` | The actual information used for retrieval |
| `category` | Category of the knowledge |
| `source` | Original source of the information |
| `version` | Version of the knowledge record |
| `pii` | Indicates whether the record contains personally identifiable information |
| `chunk_id` | Unique identifier for the searchable chunk |

## Sample Record

```text
record_id: health_basic_plan
title: Basic Health Plan
content: The Basic Health Plan provides health insurance coverage of ₹5 lakh. Annual premium is ₹7,500. Cashless hospitalization and a free annual health check-up are included. The pre-existing disease waiting period is 3 years.
category: Health Insurance
source: data/insurance.md
version: 1.0
pii: false
chunk_id: health_basic_plan_01
```

## Knowledge Categories

The insurance knowledge base is organized into the following categories:

- Health Insurance
- Life Insurance
- Motor Insurance
- Travel Insurance
- Coverage
- Eligibility
- Waiting Period
- Claims
- Required Claim Documents
- Premium Payment Methods
- Cashless Hospitals
- Policy Renewal
- Human Support

## Source Tracking

The current source document is:

```text
data/insurance.md
```

Each knowledge record should retain its source so that retrieved information can be traced back to the original material.

## PII Handling

The knowledge base contains insurance product, policy, and process information.

Customer information collected through the callback flow is kept separate from the knowledge base.

Customer lead information is stored in:

```text
leads/leads.csv
```

Knowledge-base records are marked with:

```text
pii: false
```

Real customer information should not be included in the knowledge base or public repository.

## Versioning

The initial knowledge-base version is:

```text
1.0
```

The version field allows future changes to insurance products, policies, business rules, or source material to be tracked.

## Chunking Strategy

The source document is divided into logical sections so that individual insurance topics can be retrieved independently.

Examples include:

- Individual insurance plans
- Coverage
- Eligibility
- Waiting periods
- Claim process
- Payment methods
- Policy renewal
- Human support

Each searchable section should have its own `chunk_id`.

## Product and Policy Taxonomy

The knowledge is categorized according to the insurance domain.

For example:

```text
Health Insurance
    ├── Basic Health Plan
    ├── Premium Health Plan
    └── Family Floater Plan

Life Insurance
    ├── Secure Life Plan
    └── Lifetime Protection Plan

Motor Insurance
    ├── Third Party Plan
    └── Comprehensive Motor Insurance Plan

Travel Insurance
    ├── Domestic Travel Plan
    └── International Travel Plan
```

## Embedding and Indexing

The knowledge chunks are converted into vector embeddings using:

```text
all-MiniLM-L6-v2
```

The embeddings are stored in Qdrant.

The current vector configuration uses cosine similarity.

The same embedding model is used to convert a user's question into a vector before searching the knowledge base.

## Retrieval and Ranking

The retrieval process is:

```text
User Question
      ↓
Question Embedding
      ↓
Qdrant Similarity Search
      ↓
Relevant Knowledge Chunks
      ↓
Relevance Filtering
      ↓
Context for Answer Generation
```

Retrieved results are ranked using vector similarity.

Only results meeting the configured relevance threshold are used as context for answer generation.

## Citation and Traceability

Each retrieved record should contain enough metadata to identify:

- Record ID
- Title
- Category
- Source
- Version
- Chunk ID

This allows a retrieved answer to be traced back to the source knowledge used by the retrieval system.

## Knowledge Base Maintenance

When the source information changes, the knowledge base should be re-ingested.

Before updating the index, the content should be checked for:

- Duplicate information
- Outdated information
- Inconsistent terminology
- Incorrect source content
- Personally identifiable information

The knowledge-base version should be updated when a new version is released.