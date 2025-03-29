import json
from typing import List
import numpy as np
from sklearn.manifold import TSNE
import plotly.express as px


def fold_text(text: str, length: int = 50) -> str:
    if text is None:
        return ""
    if len(text) <= length:
        return text
    return text[:length] + "..."


fd = open("data/livedoor.json")
docs = list(map(json.loads, fd))
vectors = np.load("data/vectors-livedoor-ginza.npy")
embed = TSNE(n_components=3, random_state=42).fit_transform(vectors)

texts: List[str] = list(map(lambda d: fold_text(d.get("body")), docs))
publishers: List[str] = list(map(lambda d: d.get("publisher"), docs))

fig = px.scatter_3d(
    x=embed[:, 0],
    y=embed[:, 1],
    z=embed[:, 2],
    color=publishers,
    symbol=publishers,
    hover_data=[texts],
)

fig.write_html("visualization.html")
