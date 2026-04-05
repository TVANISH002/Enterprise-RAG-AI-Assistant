````markdown
# 🚀 Enterprise RAG AI Assistant (LangChain + Streamlit + Hugging Face)

> Production-ready Retrieval-Augmented Generation (RAG) system for research papers.  
> Upload PDFs, ask questions, and get **context-aware answers** powered by LangChain and Hugging Face.

---

## 📝 Overview

This project demonstrates a **full end-to-end RAG pipeline**:

1. **PDF ingestion** → convert research papers into embeddings  
2. **Vector storage** → FAISS semantic search  
3. **RetrievalQA chain** → fetch relevant content + LLM answer generation  
4. **Interactive frontend** → Streamlit UI for uploading PDFs and asking questions  

**Goal:** Showcase full-stack GenAI engineering for **FAANG/interview-ready portfolio**.

---

## ⚡ Features

- **FastAPI backend** for ingestion and querying  
- **Streamlit frontend** for drag-and-drop PDFs and Q&A  
- **LangChain modular pipeline**: document loaders, chunkers, vectorstore, chains  
- **Open-source LLM**: Hugging Face Mistral-7B-Instruct  
- **FAISS vectorstore** for semantic retrieval  
- **Dockerized** for easy deployment  
- **Environment config** via `.env`  
- **Logging** for full observability  

---

## 🚀 Setup & Run

1. **Install dependencies**  

```bash
pip install -r requirements.txt
````

2. **Set environment variables**

```text
HF_API_KEY=your_huggingface_api_key
VECTOR_STORE_PATH=vector_store/faiss_index
CHUNK_SIZE=1000
CHUNK_OVERLAP=200
```

3. **Run backend (FastAPI)**

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

* API docs: [http://localhost:8000/docs](http://localhost:8000/docs)

4. **Run frontend (Streamlit)**

```bash
cd frontend
streamlit run app.py
```

* UI: [http://localhost:8501/](http://localhost:8501/)

5. **Optional Docker**

```bash
docker-compose up --build
```

---

## 📊 Workflow Diagram

## Demo

![Streamlit App Demo](images/demo.png)

## Architecture

![Project Architecture](images/architecture.png)



## 🧠 How It Works

1. **PDF Ingestion**

   * PyPDFLoader loads PDF pages as documents
   * RecursiveCharacterTextSplitter splits text into chunks
   * HuggingFaceEmbeddings converts chunks into vectors
   * FAISS stores vectors for fast semantic retrieval

2. **Query & Retrieval**

   * User enters question → retriever fetches top-k chunks
   * RetrievalQA chain sends chunks + question to LLM
   * LLM generates **answer grounded in PDF content**

3. **LLM**

   * **Hugging Face Mistral-7B-Instruct**

     * 7B parameters, instruction-following
     * Free, open-source, HF API compatible
     * Deterministic answers (`temperature=0`)
   * Choice ensures **real RAG pipeline demonstration without cost**

---

## 🎯 Key Concepts Demonstrated

* **RAG Pipeline**: ingestion → embeddings → retrieval → LLM → answer
* **LangChain Concepts**: document loaders, chunkers, chains, retrievers
* **Vectorstore (FAISS)**: semantic search for knowledge grounding
* **Full-stack Integration**: FastAPI + Streamlit + Docker
* **Modular, Production-ready Code**

---

## 🧪 Testing

1. Upload PDF via Streamlit or FastAPI `/ingest`
2. Query via Streamlit or FastAPI `/query?q=Your question`
3. Inspect logs for ingestion, retrieval, and LLM steps

---

## 🔗 Future Improvements

* Multi-PDF ingestion & multi-source RAG
* Show **source chunks** for transparency
* Add **Agents** for multi-step reasoning
* Deploy as **full SaaS product**

---

## 📌 References

* [LangChain Documentation](https://www.langchain.com/docs/)
* [FAISS](https://faiss.ai/)
* [Hugging Face Models](https://huggingface.co/models)

---

**Portfolio-ready project** demonstrating **RAG + LangChain + Hugging Face + FastAPI + Streamlit**

```


