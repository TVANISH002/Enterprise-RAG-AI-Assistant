```markdown
# 🔍 ResearchGPT — Production-Style RAG System for Research Papers

A modular, retrieval-augmented generation (RAG) system that converts research papers into a grounded question-answering engine.

This project focuses on **reducing hallucinations**, **improving retrieval quality**, and **designing a scalable LLM pipeline** for document intelligence.

---

## 🚀 Problem Statement

Large Language Models often generate fluent but **ungrounded answers** when applied to long-form documents like research papers.

This project solves that by:
- grounding responses in retrieved context
- structuring outputs for research understanding
- enabling scalable document querying

---

## 🧠 System Overview

```

PDF → Text Extraction → Chunking → Embedding → FAISS Index
→ Query → Query Embedding → Top-K Retrieval → Prompt Construction → LLM → Answer

```

---

## 🏗️ Architecture

### 1. Ingestion Layer
- PDF parsing using PyPDF2
- Robust handling of multi-page academic documents
- Stateless ingestion pipeline

### 2. Chunking Strategy
- Recursive / fixed-size chunking
- Tunable `chunk_size` and `overlap`
- Designed to balance:
  - semantic coherence
  - retrieval recall

### 3. Embedding Layer
- Model: `all-MiniLM-L6-v2`
- Lightweight, high-quality sentence embeddings
- Optimized for local inference

### 4. Vector Store (FAISS)
- Index: `IndexFlatL2`
- Stores dense vector representations
- Enables fast top-K similarity search

### 5. Retrieval Layer
- Query embedding → similarity search
- Returns top-K relevant chunks
- Tradeoff:
  - higher K → better recall
  - lower K → faster inference

### 6. Generation Layer
Supports two modes:

#### 🔹 Local (HuggingFace)
- Fully offline inference
- Slower, CPU-bound

#### 🔹 API-based (Groq — Recommended)
- Low-latency inference
- No model loading overhead
- Production-friendly

### 7. Prompt Engineering
Structured output enforced:

- Summary
- Method
- Key Findings
- Limitations
- Conclusion

This improves:
- readability
- evaluation consistency
- downstream usability

---

## ⚙️ Design Decisions

### Why RAG instead of Fine-Tuning?
- avoids expensive retraining
- supports dynamic document updates
- reduces hallucination via grounding

### Why FAISS?
- fast local vector search
- simple and scalable
- no external dependency required

### Why MiniLM?
- strong performance-to-size ratio
- low latency on CPU

### Why Structured Outputs?
- makes answers evaluable
- aligns with research workflows
- improves consistency across queries

---

## 📊 Evaluation Strategy

### 1. Semantic Similarity
- cosine similarity between generated and expected answers

### 2. Retrieval Quality
- manual inspection of top-K chunks
- tuning chunk size & overlap improved relevance

### 3. Hallucination Reduction
- enforced context-only prompting
- measurable improvement in grounded responses


---

## 🔑 Setup

### Environment

```bash
uv venv --python 3.11
.venv\Scripts\activate
````

### Install

```bash
uv pip install -r requirements.txt
```

---

## ▶️ Run

### Backend

```bash
uvicorn app.main:app --reload
```

### Frontend

```bash
streamlit run frontend/streamlitapp.py
```

---

## 🧪 Usage

1. Upload a research paper (PDF)
2. Ask a question
3. System retrieves relevant chunks
4. LLM generates grounded structured response

---

## 📌 Example Query

```

What is transformer architecture?

```

---

## 🧠 Example Output

```

Summary:
Transformers are sequence models based on self-attention.

Method:
They use encoder-decoder architecture with multi-head attention.

Key Findings:
- No recurrence required
- Parallel computation
- State-of-the-art performance

Limitations:
Depends on retrieved context quality.

Conclusion:
Transformers replace recurrence with attention mechanisms.

```

---

## 🚀 Extensions (Next Steps)

* LoRA / PEFT fine-tuned generation layer
* Hybrid search (BM25 + vector)
* Citation-level grounding
* Multi-document reasoning
* Caching & latency optimization

---
