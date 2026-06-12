import faiss
import pickle
from sentence_transformers import SentenceTransformer

index = faiss.read_index("shakespeare_index.faiss")
with open("quotes.pkl", "rb") as f:
    quotes = pickle.load(f)

model = SentenceTransformer("all-MiniLM-L6-v2")

def search_quotes(query, top_k=1):
    query_vec = model.encode([query])
    distances, indices = index.search(query_vec, top_k)
    return [quotes[i] for i in indices[0]]
