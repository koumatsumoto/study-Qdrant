import numpy as np
import json
from qdrant_client import QdrantClient

fd = open('data/livedoor.json')
vectors = np.load('data/vectors-livedoor-ginza.npy')

docs = []
for line in fd.readlines(): # ペイロードの用意
    docs.append(json.loads(line))

collection_name = 'livedoor'
qdrant_client = QdrantClient(host='localhost', port=6333)


qdrant_client.upload_collection(
    collection_name=collection_name, # コレクション名
    vectors=vectors, # ベクトルデータ
    payload=iter(docs), # ペイロードデータ
    ids=None,  # IDの自動発番
    batch_size=256  # バッチサイズ
)
