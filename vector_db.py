import pinecone
from embed import get_embedding

# Paste your Pinecone details
API_KEY = "pcsk_4JZxte_QCkziZvoWRbzDJvfJGuRHcmnkQKmYskyEtzuNDsrCJiiJEY2FNz3ccm9bf3dxG8"
ENV = "us-east-1"
INDEX_NAME = "assistant-db"

pinecone.init(api_key=API_KEY, environment=ENV)

# Create index (run only once)
if INDEX_NAME not in pinecone.list_indexes():
    pinecone.create_index(
        name=INDEX_NAME,
        dimension=384,
        metric="cosine"
    )

index = pinecone.Index(INDEX_NAME)


# Add data
def add_data(text, id):
    vector = get_embedding(text)

    index.upsert([
        (id, vector, {"text": text})
    ])


# Search
def search_data(query):
    vector = get_embedding(query)

    result = index.query(
        vector=vector,
        top_k=3,
        include_metadata=True
    )

    return result
