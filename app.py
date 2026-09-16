from flask import Flask, request, jsonify, render_template
from src.preprocess import preprocess_text
from src.embed import get_clause_vector
from src.similarity import find_similar_clauses
from src.utils import load_models
import numpy as np

app = Flask(__name__)

model, clauses, clause_vectors = load_models()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "online", "model_loaded": True, "vocabulary_size": len(model.wv), "clauses": len(clauses)})

@app.route("/search", methods=["POST"])
def search():
    data = request.get_json(silent=True) or {}
    query = data.get("query", "").strip()
    top_k = int(data.get("top_k", 5))

    if not query:
        return jsonify({"error": "Please enter a legal clause."}), 400

    if top_k < 1:
        top_k = 1

    if top_k > 20:
        top_k = 20

    tokens = preprocess_text(query)

    if not tokens:
        return jsonify({"error": "No meaningful words found in the query."}), 400

    query_vector = get_clause_vector(tokens, model)

    if not np.any(query_vector):
        return jsonify({"error": "The query contains no words known by the Word2Vec model."}), 400

    results = find_similar_clauses(query_vector, clause_vectors, clauses, top_k)

    return jsonify({"query": query, "results": results})

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)