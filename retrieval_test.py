import os

from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient

load_dotenv()

COLLECTION = "insurance_knowledge"

model = SentenceTransformer("all-MiniLM-L6-v2")

client = QdrantClient(
    url=os.getenv("QDRANT_URL").strip(),
    api_key=os.getenv("QDRANT_API_KEY").strip(),
    timeout=60,
    check_compatibility=False
)


TEST_QUERIES = [
    "What is the Basic Health Plan premium?",
    "What is the waiting period for pre-existing diseases?",
    "What documents are required for a claim?",
    "Can I pay my premium using UPI?",
    "I want to speak with a human insurance advisor."
]


def run_test(question):

    vector = model.encode(question).tolist()

    results = client.query_points(
        collection_name=COLLECTION,
        query=vector,
        limit=3
    ).points

    print("\n" + "=" * 70)
    print(f"QUESTION: {question}")
    print("=" * 70)

    if not results:
        print("No results found.")
        return

    for rank, result in enumerate(results, start=1):

        payload = result.payload

        print(f"\nResult {rank}")
        print("-" * 50)
        print(f"Score:      {result.score:.4f}")
        print(f"Record ID:  {payload.get('record_id')}")
        print(f"Title:      {payload.get('title')}")
        print(f"Category:   {payload.get('category')}")
        print(f"Source:     {payload.get('source')}")
        print(f"Version:    {payload.get('version')}")
        print(f"Chunk ID:   {payload.get('chunk_id')}")
        print(f"PII:        {payload.get('pii')}")
        print("\nRetrieved content:")
        print(payload.get("content", ""))


for query in TEST_QUERIES:
    run_test(query)