import os
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct

load_dotenv()

COLLECTION = "insurance_knowledge"

model = SentenceTransformer("all-MiniLM-L6-v2")

client = QdrantClient(
    url=os.getenv("QDRANT_URL").strip(),
    api_key=os.getenv("QDRANT_API_KEY").strip(),
    timeout=120,
    check_compatibility=False
)

with open("data/insurance.md", "r", encoding="utf-8") as f:
    text = f.read()

# Better chunking
sections = text.split("---")

chunks = []

for section in sections:
    section = section.strip()
    if len(section) > 50:
        chunks.append(section)

try:
    client.delete_collection(COLLECTION)
except:
    pass

client.create_collection(
    collection_name=COLLECTION,
    vectors_config=VectorParams(
        size=384,
        distance=Distance.COSINE
    )
)

points = []

for i, chunk in enumerate(chunks):
    vector = model.encode(chunk).tolist()

    points.append(
        PointStruct(
            id=i,
            vector=vector,
            payload={
                "text": chunk
            }
        )
    )

client.upsert(
    collection_name=COLLECTION,
    points=points,
    wait=True
)

print(f"Uploaded {len(points)} chunks successfully.")