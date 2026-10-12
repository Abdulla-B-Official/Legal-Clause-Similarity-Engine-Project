# Legal Clause Similarity Engine Project

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Web_Framework-000000?style=for-the-badge&logo=flask&logoColor=white)
![NLP](https://img.shields.io/badge/NLP-Word2Vec_%7C_Cosine_Similarity-yellow?style=for-the-badge)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6%2B-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)

<p align="center">
  <b>A specialized Natural Language Processing (NLP) legal tech engine designed to parse, embed, and match legal clauses and contractual terms using Word2Vec embeddings and a Flask web application.</b>
</p>

---

## Overview

The **Legal Clause Similarity Engine** is an advanced NLP application built to assist legal professionals and contract reviewers in identifying matching clauses, risk exposure, and legal precedents. 

The system features a structured backend pipeline located in `src/` for text preprocessing, embedding calculation via Word2Vec, and similarity scoring, paired with an interactive frontend dashboard via Flask templates:

* **Text Preprocessing (`preprocess.py`):** Cleans and normalizes legal terminology, statutory citations, and multi-clause text inputs.
* **Vector Embeddings (`embed.py`):** Generates and serializes vector representations using trained Word2Vec models (`word2vec_model.pkl`).
* **Similarity Search Engine (`similarity.py`):** Computes precise cosine similarity to rank corresponding clauses from the dataset (`class_vectors.pkl` and `classes.pkl`).
* **Web Interface (`app.py`):** A lightweight Flask application rendering dynamic HTML templates and handling asynchronous frontend requests.

---

## Repository Structure

```text
legal-clause-similarity-engine-project/
├── models/
│   ├── class_vectors.pkl      # Serialized clause vector space
│   ├── classes.pkl            # Indexed legal clause metadata/labels
│   └── word2vec_model.pkl     # Trained Word2Vec embedding binary
├── src/
│   ├── __pycache__/
│   ├── embed.py               # Vector generation & embedding script
│   ├── preprocess.py          # Legal text cleaning & normalization
│   ├── similarity.py          # Cosine similarity ranking engine
│   └── utils.py               # Helper utility functions
├── static/
│   ├── css/
│   │   └── style.css          # Dashboard styling
│   └── js/                    # Frontend script interactions
├── templates/
│   └── index.html             # Main user interface template
├── .gitignore                 # Git exclusion rules
├── app.py                     # Flask web server entry point
├── README.md                  # Project documentation
└── requirements.txt           # Python dependencies

```

---

## System Architecture

$$\text{Legal Clause Query} \longrightarrow \text{Preprocessing (`preprocess.py`)} \longrightarrow \text{Word2Vec Embedding (`embed.py`)} \longrightarrow \text{Similarity Matrix (`similarity.py`)} \longrightarrow \text{Flask Web UI}$$

1. **User Input:** Input query entered through `templates/index.html`.
2. **Preprocessing:** Text is scrubbed and tokenized via `src/preprocess.py`.
3. **Vectorization & Matching:** The query vector is evaluated against stored pickles in `models/` using `src/similarity.py`.
4. **Result Presentation:** Ranked clause suggestions with similarity scores are rendered back to the user interface.

---

## Installation & Setup

### 1. Clone the Repository

```bash
git clone [https://github.com/Abdulla-B-Official/Legal-Clause-Similarity-Engine-Project.git](https://github.com/Abdulla-B-Official/Legal-Clause-Similarity-Engine-Project.git)
cd Legal-Clause-Similarity-Engine-Project

```

### 2. Set Up Virtual Environment

```bash
python -m venv .venv
# Activate on Windows PowerShell:
.venv\Scripts\Activate.ps1
# Activate on Linux/macOS:
source .venv/bin/activate

```

### 3. Install Dependencies

```bash
pip install -r requirements.txt

```

### 4. Run the Web Application

```bash
python app.py

```

Open your browser and navigate to `http://127.0.0.1:5000` to interact with the system.

```

```
