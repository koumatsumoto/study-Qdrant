from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance

collection_name = 'livedoor'
qdrant_client = QdrantClient(host='localhost', port=6333)


qdrant_client.delete_collection(
    collection_name=collection_name # コレクション名
)

qdrant_client.recreate_collection(
  collection_name=collection_name,
  vectors_config=VectorParams(size=300, distance=Distance.COSINE) # GiNZAは300次元
)
