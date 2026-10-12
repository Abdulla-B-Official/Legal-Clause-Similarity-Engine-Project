# Legal Clause Similarity Engine Project

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Web_Framework-000000?style=for-the-badge&logo=flask&logoColor=white)
![NLP](https://img.shields.io/badge/NLP-Sentence_Transformers-yellow?style=for-the-badge)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6%2B-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)

<p align="center">
  <b>A specialized Natural Language Processing (NLP) legal tech engine designed to parse, embed, and match legal clauses, contractual terms, and regulatory provisions using dense vector representations and a web-based dashboard.</b>
</p>

---

<p align="center">
  <img src="https://img.shields.io/badge/Domain-Legal_Tech_%26_Contract_Analysis-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Embedding-Transformer_Models-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Metrics-Cosine_Similarity-orange?style=for-the-badge" />
</p>

---

## Overview

The **Legal Clause Similarity Engine** is an advanced NLP application built to assist legal professionals, compliance officers, and contract managers in analyzing legal agreements. By transforming complex statutory language and contract clauses into dense vector embeddings, the system goes beyond keyword matching to uncover conceptual alignment, risk exposure, and precedent similarities across large document repositories.

The system features a robust Python backend for legal text preprocessing, embedding calculation, and similarity scoring, paired with an interactive web UI for immediate clause comparison:

* **Legal Text Preprocessing:** Custom cleaning routines tailored to parse dense legal jargon, section headers, statutory references, and multi-clause formatting.
* **Dense Semantic Embeddings:** Converts contractual clauses into high-dimensional vectors to capture underlying legal intent, liabilities, and obligations.
* **Similarity Retrieval Engine:** Computes precise cosine similarity and distance metrics to rank corresponding historical clauses or standard templates.
* **Interactive Web Interface:** A responsive dashboard allowing users to input target legal text and instantly visualize matching clauses along with confidence scores.

---

## Application Features

* **Contextual Legal Analysis:** Identifies semantic matches between differently phrased clauses that share identical legal obligations (e.g., matching *"limitation of liability"* variations).
* **Full-Stack Architecture:** Modular separation between the analytical Python backend engine and the dynamic client-facing web application.
* **Fast and Scalable:** Optimized retrieval pipelines to scan and match clauses against structured legal databases in milliseconds.
* **Clean Codebase Organization:** Structured directories for data ingestion, embedding generation, search logic, and UI asset management.

---

## Repository Structure

```text
Legal-Clause-Similarity-Engine-Project/
├── backend/
│   ├── data/                 # Dataset containing legal clauses and contracts
│   ├── embeddings/           # Clause vector generation and indexing logic
│   ├── models/               # Saved model weights and cached vectors
│   ├── preprocessing/        # Legal text tokenization and normalization
│   ├── search/               # Cosine similarity and ranking search engine
│   ├── training/             # Model fine-tuning or training scripts
│   └── config.py             # Global configurations, paths, and parameters
├── frontend/
│   ├── css/                  # Interface styling and theme assets
│   ├── js/                   # Asynchronous fetch and DOM event handlers
│   └── index.html            # Main dashboard user interface
├── .gitignore                # Git exclusion rules for caches and models
├── app.py                    # Flask server entry point
├── README.md                 # Project documentation
└── requirements.txt          # Python dependencies

```

---

## System Architecture

$$\text{Legal Clause Input} \longrightarrow \text{Text Normalization} \longrightarrow \text{Dense Vector Embedding} \longrightarrow \text{Similarity Matrix Engine} \longrightarrow \text{Ranked Clause Results UI}$$

1. **Clause Input:** User pastes a contractual clause or regulatory requirement into the web dashboard.
2. **Text Normalization:** The preprocessing pipeline cleans text, strips artifacts, and prepares the text block.
3. **Vectorization:** The text is mapped into semantic space using pre-trained transformer embeddings.
4. **Similarity Engine:** The backend computes similarity scores against the indexed legal corpus.
5. **Dashboard Presentation:** Relevant clauses and match percentages are rendered dynamically on the frontend interface.

---

## Installation & Setup

### 1. Clone the Repository

```bash
git clone [https://github.com/Abdulla-B-Official/Legal-Clause-Similarity-Engine-Project.git](https://github.com/Abdulla-B-Official/Legal-Clause-Similarity-Engine-Project.git)
cd "Legal-Clause-Similarity-Engine-Project"

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

Open your browser and navigate to `http://127.0.0.1:5000` to interact with the legal clause similarity dashboard.

```

```
