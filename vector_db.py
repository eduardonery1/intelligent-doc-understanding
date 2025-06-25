import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer

class VectorDB:
    def __init__(self, model_name="all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)
        self.index = faiss.read_index("doc_index.faiss")
        with open("doc_metadata.pkl", "rb") as f:
            self.metadata = pickle.load(f)

    def predict_type(self, text: str):
        embedding = self.model.encode(text).astype("float32").reshape(1, -1)
        D, I = self.index.search(embedding, k=1)
        best_idx = I[0][0]
        doc_type = self.metadata[best_idx]
        confidence = 1 / (1 + D[0][0])
        return doc_type, confidence

