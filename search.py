from qdrant_client import QdrantClient
from random import randrange
import numpy as np
import json

fd = open("data/livedoor.json")
vectors = np.load("data/vectors-livedoor-ginza.npy")

docs = []
for line in fd.readlines():  # ペイロードの用意
    docs.append(json.loads(line))

collection_name = "livedoor"
qdrant_client = QdrantClient(host="localhost", port=6333)


idx = randrange(
    len(vectors)
)  # クエリーに使用するドキュメントのベクトルをランダムに取得
print(docs[idx].get("body"))

hits = qdrant_client.search(
    collection_name=collection_name,
    query_vector=vectors[idx],  # クエリーベクトル
    query_filter=None,
    with_payload=True,  # レスポンスにペイロードを含める
    limit=5,  # 上位の5件を取得
)

for hit in hits:  # レスポンスデータ
    h = hit
    print(f"{h.score} - {h.payload.get('body')}")
