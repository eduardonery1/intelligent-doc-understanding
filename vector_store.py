from sentence_transformers import SentenceTransformer
from ocr import OCR
import faiss
import numpy as np
import pickle
from pathlib import Path
from tqdm import tqdm
from PIL import Image

base_path = Path('docs-sm')

# Load model
model = SentenceTransformer('all-MiniLM-L6-v2')
ocr_reader = OCR()

# Build embeddings and metadata
embeddings = []
metadata = []

for filepath in tqdm(list(base_path.glob("*/*.jpg"))):
    with open(filepath, "rb") as f:
        img = Image.open(f)

        text = ocr_reader.extract_text_from_image(img)
        emb = model.encode(text)
        embeddings.append(emb)

        doc_class = filepath.parent.stem
        metadata.append(doc_class)

# Save index + metadata
embedding_matrix = np.array(embeddings).astype('float32')
index = faiss.IndexFlatL2(embedding_matrix.shape[1])
index.add(embedding_matrix)

faiss.write_index(index, "doc_index.faiss")
with open("doc_metadata.pkl", "wb") as f:
    pickle.dump(metadata, f)

