from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from config import EMBEDDING_MODEL, CHROMA_DIR

def create_vector_store(documents):
    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)

    db = Chroma.from_documents(
        documents=documents,
        embedding=embeddings,
        persist_directory=CHROMA_DIR,
        collection_metadata={"hnsw:space": "cosine"},
    )

    print("✅ Vector store created")
    return db
