import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def find_similar_clauses(query_vector, clause_vectors, clauses, top_k=5):
    similarities = cosine_similarity(query_vector.reshape(1, -1), clause_vectors)[0]

    top_indices = np.argsort(similarities)[-top_k:][::-1]

    results = []

    for rank, index in enumerate(top_indices, start=1):
        results.append({"rank": rank, "clause": clauses.iloc[index]["clause_text"], "category": clauses.iloc[index]["clause_type"], "similarity": round(float(similarities[index]), 4)})

    return results