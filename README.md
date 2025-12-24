# Multimodal RAG Document Intelligence System

A production-grade **Multi-Modal Retrieval-Augmented Generation (RAG)** pipeline that can understand, index, and answer questions from **complex PDF documents** containing **text, tables, and images**.

This system leverages **Unstructured.io** for high-resolution document parsing, **AI-generated searchable summaries**, and **Chroma vector storage** for semantic retrieval, enabling accurate question answering over research papers and enterprise documents.

---

## 🚀 Key Features

- 📄 **High-Resolution PDF Parsing**
  - Extracts text, tables (as HTML), and images from PDFs
  - Uses `Poppler`, `Tesseract OCR`, and `libmagic`

- 🧩 **Intelligent Chunking**
  - Title-based semantic chunking
  - Preserves original elements (tables & images)

- 🧠 **AI-Enhanced Chunk Summarization**
  - Uses Gemini Vision models
  - Converts mixed content (text + tables + images) into searchable descriptions

- 🔍 **Vector Search with Chroma**
  - Sentence-Transformers embeddings
  - Persistent vector database

- 🤖 **Multimodal Question Answering**
  - Uses retrieved chunks + original tables & images
  - Grounded answers with fallback handling

---

## 🏗️ Architecture Overview

- PDF Document
- Unstructured.io (hi_res parsing)
- Title-based Chunking
- AI-Enhanced Summaries (Gemini)
- Vector Embeddings (HuggingFace)
- Chroma Vector Store
- Multimodal RAG Answering


---

## 🛠 Tech Stack

- **Python**
- **Unstructured.io**
- **LangChain**
- **Google Gemini (Vision + Text)**
- **HuggingFace Sentence Transformers**
- **Chroma Vector Database**
- **Tesseract OCR**
- **Poppler**

---

## 📦 Installation

### 1️⃣ System Dependencies

#### Ubuntu / Debian
```bash
sudo apt update
sudo apt install poppler-utils tesseract-ocr libmagic-dev -y
```

### Windows

Install Poppler and add to PATH

Install Tesseract OCR and add to PATH

Install libmagic via python-magic-bin

### 2️⃣ Python Dependencies
```bash
pip install -r requirements.txt
```
### 3️⃣ Environment Variables

Create a .env file:
```bash
GOOGLE_API_KEY=your_gemini_api_key_here
```
---

### 📤 Output Artifacts

chunks_export.json → AI-enhanced chunk summaries

rag_results.json → Retrieved chunks for a query

db/chroma_db/ → Persistent vector store

### 🎯 Use Cases

Research paper analysis

Enterprise document search

Financial & legal document QA

Knowledge base creation

Multimodal AI assistants
