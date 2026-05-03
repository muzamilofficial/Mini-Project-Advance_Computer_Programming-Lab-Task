from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as np
import re
import faiss
from sentence_transformers import SentenceTransformer

app = Flask(__name__)

# ── 1. Load CSV data ──────────────────────────────────────────────────────────
DATA_FILE = 'restaurant_data.csv'
restaurant_df = pd.read_csv(DATA_FILE)

# ── 2. Clean text (same as notebook) ─────────────────────────────────────────
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)   # remove punctuation
    text = re.sub(r'\s+', ' ', text)               # remove extra spaces
    return text.strip()

restaurant_df['Cleaned_Answer'] = restaurant_df['answer'].astype(str).apply(clean_text)

# ── 3. Load SentenceTransformer model ─────────────────────────────────────────
print("Loading embedding model...")
embed_model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

# ── 4. Encode answers & build FAISS index ─────────────────────────────────────
print("Building FAISS index...")
answer_embeddings = embed_model.encode(
    restaurant_df['Cleaned_Answer'].values,
    show_progress_bar=True
).astype('float32')

np.save('restaurant_embeddings.npy', answer_embeddings)      # save embeddings
answer_embeddings = np.load('restaurant_embeddings.npy')     # load back

vec_dim    = answer_embeddings.shape[1]
faiss_idx  = faiss.IndexFlatL2(vec_dim)                      # Euclidean distance
faiss_idx.add(answer_embeddings)
faiss.write_index(faiss_idx, 'faiss_index.index')            # save index

print(f"FAISS index ready — {faiss_idx.ntotal} answers indexed.")

# ── 5. Retrieve best matching answer ─────────────────────────────────────────
THRESHOLD = 1.8   # L2 distance limit — increase to allow fuzzier matches

def get_best_answer(user_query, top_k=1):
    cleaned_q = clean_text(user_query)
    q_vec     = embed_model.encode([cleaned_q]).astype('float32')

    distances, indices = faiss_idx.search(q_vec, top_k)

    best_dist = distances[0][0]
    best_idx  = indices[0][0]

    if best_dist > THRESHOLD:
        return (
            "Sorry, I could not find a matching answer. "
            "Try asking about our <b>menu</b>, <b>timings</b>, "
            "<b>reservation</b>, <b>delivery</b>, <b>specials</b>, or <b>location</b>.",
            "Unknown"
        )

    answer   = restaurant_df['answer'].iloc[best_idx]
    category = restaurant_df['category'].iloc[best_idx]
    return answer, category

# ── 6. Flask routes ───────────────────────────────────────────────────────────
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def get_response():
    user_msg = request.form.get("msg", "").strip()
    if not user_msg:
        return jsonify({"response": "Please type a question.", "category": ""})

    answer, category = get_best_answer(user_msg)
    return jsonify({"response": answer, "category": category})

if __name__ == "__main__":
    app.run(debug=True)
