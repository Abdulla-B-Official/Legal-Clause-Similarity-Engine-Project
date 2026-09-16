# Legal Clause Similarity Engine

![Python](https://img.shields.io/badge/Python-45.7%25-3776AB?style=for-the-badge&logo=python&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-23.6%25-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![CSS](https://img.shields.io/badge/CSS-16.9%25-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![HTML](https://img.shields.io/badge/HTML-13.8%25-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github&logoColor=white)

<p align="center">
  <b>A full-stack Natural Language Processing (NLP) semantic search application designed to analyze, compare, and retrieve similar legal clauses from extensive contract repositories using a Python backend and an interactive web frontend.</b>
</p>

---

<p align="center">
  <img src="https://img.shields.io/badge/Algorithm-Semantic_Similarity-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Architecture-Full--Stack_NLP-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Handling-Legal_Text_Normalization-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Metrics-Cosine_Similarity_Scores-red?style=for-the-badge" />
</p>

---

## Overview

**Legal Clause Similarity Engine** is an NLP-driven document analysis pipeline and web application built to process unstructured legal contracts, automatically comparing uploaded or drafted clauses against a standardized database to identify semantic matches, deviations, and boilerplate language.

The system leverages a robust Python backend for high-performance text vectorization and similarity computation, paired with a responsive HTML/CSS/JS frontend for seamless user interaction:

* **Text Preprocessing & Normalization:** Legal jargon standardization, punctuation stripping, tokenization, and formatting normalization.
* **Feature Extraction & Embedding:** Converting complex legal phrasing into numerical vector representations to capture deep contextual meaning rather than just exact keyword matches.
* **Similarity Computation:** Utilizing distance metrics (like Cosine Similarity) to calculate mathematical overlaps between the queried clause and the existing legal database.
* **Interactive User Interface:** A dynamic web front-end enabling legal professionals to input text, adjust search thresholds, and instantly visualize matched clauses and similarity scores.

The system transforms dense legal text into mathematically comparable vectors, bridging the gap between raw unstructured contracts and automated risk assessment.

---

### Language Breakdown

| Language | Percentage | Primary Usage |
| :--- | :--- | :--- |
| **Python** | **45.7%** | Core NLP pipeline, text preprocessing, vector embedding, similarity computation, and backend API routing |
| **JavaScript** | **23.6%** | Asynchronous API communication, dynamic DOM updates, and interactive frontend logic for displaying results |
| **CSS** | **16.9%** | Application styling, responsive layout design, and visual hierarchy for readable legal text comparisons |
| **HTML** | **13.8%** | Structural markup for the user interface, input forms, and result dashboards |

---

### Application Features

* **Full-Stack Architecture:** Clean separation between the NLP processing backend (Python) and the user-facing web interface (JS/HTML/CSS).
* **Semantic Search Capabilities:** Goes beyond basic `CTRL+F` keyword matching to understand the contextual intent of legal phrasing (e.g., matching "force majeure" with "act of God").
* **Real-Time Similarity Scoring:** Instantly calculates and displays percentage-based confidence scores for how closely a queried clause matches standard templates.
* **Legal Text Normalization:** Preserves critical legal definitions while stripping uninformative noise, formatting artifacts, and OCR errors.
* **Interactive Result Dashboard:** Highlights matched terms and allows users to easily copy, review, or flag standard vs. non-standard contract clauses.

---

## Project Objective

The primary objective is to build a scalable, user-friendly legal tech solution that can:

* Clean, normalize, and structure unstructured contract clauses from various legal documents.
* Vectorize text to capture the semantic nuances of legal language.
* Compute similarity scores to detect deviations from standard company boilerplate language.
* Provide an intuitive web interface for legal teams to search and compare clauses without requiring technical expertise.
* Accelerate the contract review process and reduce the risk of non-standard obligations slipping into agreements.

---

## Problem Statement

Reviewing hundreds of pages of contracts to ensure clauses align with standard company policies is a tedious, error-prone, and expensive manual process. Traditional keyword searches fail because opposing counsels frequently use synonyms or rephrase standard concepts.

Standard baseline solutions frequently suffer from:

* An inability to detect semantic similarity when different vocabulary is used to describe the same legal mechanism.
* Cumbersome, non-technical workflows that force lawyers to compare documents side-by-side manually.
* A lack of intuitive UI, rendering powerful backend NLP models useless to the actual end-users who need them.

### Proposed Solution

This project introduces a robust full-stack NLP pipeline executing:

$$\text{Raw Legal Clause} \longrightarrow \text{Text Normalization} \longrightarrow \text{Vector Embedding} \longrightarrow \text{Similarity Computation} \longrightarrow \text{Matched Clauses \& Scores}$$

For every legal clause processed through the web interface, the system produces:

```text
Cleaned & Standardized Text
Ranked List of Matched Database Clauses
Percentage-Based Similarity Scores
Visual Dashboard Output for Fast Review
