# Data Collection and Cleaning

## Source

The current insurance knowledge source is:

```text
data/insurance.md
```

The source contains information about Darwix Insurance products, coverage, eligibility, waiting periods, claims, payment methods, policy renewal and human support.

## Collection

The insurance information is maintained as a Markdown knowledge-base document.

The ingestion process reads the source document before creating searchable knowledge records.

## Parsing

The Markdown document is read as UTF-8 text.

The current ingestion process separates the document into logical sections using the section separators present in the source.

Each meaningful section becomes a candidate knowledge chunk.

## Cleaning

The knowledge content should be checked before indexing for:

- Empty sections
- Repeated content
- Unnecessary formatting
- Duplicate information
- Outdated information
- Inconsistent terminology
- Irrelevant text

Very small or empty sections should not be indexed as knowledge records.

## Duplicate Handling

Duplicate or repeated knowledge should be identified before indexing.

Where the same information appears more than once, duplicate content should be removed so that retrieval does not return repeated results.

## Standardized Terminology

Insurance categories and product names should remain consistent throughout the knowledge base.

Examples include:

- Health Insurance
- Life Insurance
- Motor Insurance
- Travel Insurance
- Basic Health Plan
- Premium Health Plan
- Family Floater Plan
- Secure Life Plan
- Lifetime Protection Plan
- Third Party Plan
- Comprehensive Motor Insurance Plan
- Domestic Travel Plan
- International Travel Plan

## PII Handling

The knowledge base is intended to contain insurance information rather than customer-specific information.

Customer information collected through the callback workflow is kept separate from the knowledge base.

The callback data is stored in:

```text
leads/leads.csv
```

Real customer information should not be included in the public knowledge base or repository.

## Validation Before Indexing

Before content is indexed, the data should be checked for:

1. Missing or empty content
2. Duplicate information
3. Inconsistent terminology
4. Irrelevant content
5. Accidental PII
6. Incorrect or outdated information

Only valid and relevant knowledge should be sent to the embedding and retrieval pipeline.