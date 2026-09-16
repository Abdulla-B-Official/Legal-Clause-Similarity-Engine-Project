import pickle
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_DIR = BASE_DIR / "models"

def load_models():
    with open(MODEL_DIR / "word2vec_model.pkl", "rb") as file:
        model = pickle.load(file)

    with open(MODEL_DIR / "classes.pkl", "rb") as file:
        clauses = pickle.load(file)

    with open(MODEL_DIR / "class_vectors.pkl", "rb") as file:
        clause_vectors = pickle.load(file)

    return model, clauses, clause_vectors