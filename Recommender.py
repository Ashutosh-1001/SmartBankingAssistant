# src/recommender.py
from sentence_transformers import SentenceTransformer
import numpy as np
import faiss
from db_connect import get_all_products
import os

# load model once
EMB_MODEL = os.getenv("EMB_MODEL", "all-MiniLM-L6-v2")
embedder = SentenceTransformer(EMB_MODEL)

class SimpleRecommender:
    def __init__(self):
        self.products = get_all_products()
        self.index = None
        self.embeddings = None
        if self.products:
            self._build_index()

    def _build_index(self):
        texts = [ (p["ProductName"] + " " + (p.get("Description") or "")) for p in self.products]
        embs = embedder.encode(texts, convert_to_numpy=True)
        d = embs.shape[1]
        self.index = faiss.IndexFlatL2(d)
        self.index.add(embs)
        self.embeddings = embs

    def recommend(self, customer_profile, top_k=3):
        # Create a short query text from customer profile
        query = f"{customer_profile['Age']} years old, balance {customer_profile['CurrentBalance']}, risk {customer_profile['RiskProfile']}, spends {customer_profile['AverageMonthlySpending']} monthly"
        q_emb = embedder.encode([query], convert_to_numpy=True)
        D, I = self.index.search(q_emb, top_k)
        results = []
        for idx in I[0]:
            p = self.products[int(idx)]
            results.append(p)
        return results

# Optional: LLM-based explanation (placeholder)
def explain_with_llm(customer_profile, product):
    # Placeholder - integrate OpenAI / LangChain as needed.
    # Example pseudo-step: send prompt describing customer + product -> LLM returns explanation.
    # Here we return a simple templated explanation.
    return f"Product '{product['ProductName']}' suits the customer's profile (risk={customer_profile['RiskProfile']}, balance={customer_profile['CurrentBalance']})."

# Usage:
# rec = SimpleRecommender(); rec.recommend(customer_dict)
