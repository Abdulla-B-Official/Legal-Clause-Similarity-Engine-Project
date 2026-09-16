import re
import string
import spacy
from nltk.corpus import stopwords

nlp = spacy.load("en_core_web_sm")

stop_words = set(stopwords.words("english"))
legal_words = {"shall", "not", "no", "without", "unless", "except", "all"}
stop_words = stop_words - legal_words

def preprocess_text(text):
    if not isinstance(text, str):
        return []

    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    text = re.sub(r"\d+", "", text)
    text = re.sub(r"\s+", " ", text).strip()

    doc = nlp(text)

    tokens = [token.lemma_ for token in doc if not token.is_space and token.lemma_ not in stop_words]

    return tokens