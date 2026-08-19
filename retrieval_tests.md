# Retrieval Evaluation

## Purpose

The retrieval pipeline was tested using five representative insurance
questions covering product information, policy information, claims, payments,
and human assistance.

The tests verify whether the correct knowledge record is retrieved from Qdrant
and whether the retrieved information is relevant to the question.

## Test 1 — Basic Health Plan Premium

### Query

What is the Basic Health Plan premium?

### Retrieved Record

- Record ID: `health_insurance_basic_health_plan_1`
- Title: `Basic Health Plan`
- Category: `Health Insurance`
- Source: `data/insurance.md`
- Version: `1.0`
- Chunk ID: `health_insurance_basic_health_plan_1_01`
- Similarity Score: `0.7508`

### Retrieved Information

The Basic Health Plan provides ₹5 lakh of health insurance coverage and has an
annual premium of ₹7,500.

It also includes cashless hospitalization, a free annual health check-up, and
a 3-year pre-existing disease waiting period.

### Relevance

The top retrieved record directly contains the requested premium information
and is the correct source for the question.

### Verdict

**Correct**

---

## Test 2 — Pre-existing Disease Waiting Period

### Query

What is the waiting period for pre-existing diseases?

### Retrieved Record

- Record ID: `health_insurance_waiting_period_12`
- Title: `Waiting Period`
- Category: `Health Insurance`
- Source: `data/insurance.md`
- Version: `1.0`
- Chunk ID: `health_insurance_waiting_period_12_01`
- Similarity Score: `0.5649`

### Retrieved Information

Pre-existing diseases have a waiting period of 3 years under the Basic Health
Plan.

### Relevance

The retrieved Waiting Period record directly answers the question and also
contains related waiting-period information.

### Verdict

**Correct**

---

## Test 3 — Claim Documents

### Query

What documents are required for a claim?

### Retrieved Record

- Record ID: `claims_required_claim_documents_14`
- Title: `Required Claim Documents`
- Category: `Claims`
- Source: `data/insurance.md`
- Version: `1.0`
- Chunk ID: `claims_required_claim_documents_14_01`
- Similarity Score: `0.5973`

### Retrieved Information

The retrieved record lists the documents that may be required for a claim,
including:

- Policy number
- Aadhaar Card
- PAN Card
- Identity proof
- Medical bills
- Accident documents
- Bank account details

### Relevance

The top result directly matches the customer's question and provides the
required claim-document information.

### Verdict

**Correct**

---

## Test 4 — UPI Payment

### Query

Can I pay my premium using UPI?

### Retrieved Record

- Record ID: `premium_payment_methods_premium_payment_methods_15`
- Title: `Premium Payment Methods`
- Category: `Premium Payment Methods`
- Source: `data/insurance.md`
- Version: `1.0`
- Chunk ID: `premium_payment_methods_premium_payment_methods_15_01`
- Similarity Score: `0.6617`

### Retrieved Information

UPI is listed as an available premium payment method.

Other available methods include debit card, credit card, net banking, and
auto debit.

Premiums can be paid monthly or yearly.

### Relevance

The top retrieved record directly contains the requested UPI payment
information.

### Verdict

**Correct**

---

## Test 5 — Human Advisor

### Query

I want to speak with a human insurance advisor.

### Retrieved Record

- Record ID: `human_support_human_support_18`
- Title: `Human Support`
- Category: `Human Support`
- Source: `data/insurance.md`
- Version: `1.0`
- Chunk ID: `human_support_human_support_18_01`
- Similarity Score: `0.6212`

### Retrieved Information

Customers can request a callback, an insurance advisor, or assistance
comparing plans.

### Relevance

The top result directly matches the customer's request for human assistance.

### Verdict

**Correct**

---

## Evaluation Summary

| Test | Query Type | Top Result | Score | Verdict |
|---|---|---|---:|---|
| 1 | Product | Basic Health Plan | 0.7508 | Correct |
| 2 | Policy | Waiting Period | 0.5649 | Correct |
| 3 | Claims | Required Claim Documents | 0.5973 | Correct |
| 4 | Payment | Premium Payment Methods | 0.6617 | Correct |
| 5 | Human Support | Human Support | 0.6212 | Correct |

## Observations

All five test queries returned a relevant top-ranked knowledge record.

The retrieved records include metadata for source traceability, including record
ID, category, source, version, and chunk ID.

The results demonstrate that the knowledge base can retrieve relevant
information for different types of insurance questions.

Further evaluation with a larger test set would be required before production
deployment.