from ingestion.partitioner import partition_documents
from ingestion.chunker import create_chunks_by_title
from processing.summarizer import summarise_chunks
from vectorstore.chroma_store import create_vector_store

def run_ingestion_pipeline(pdf_path: str):

    elements = partition_documents(pdf_path)

    chunks = create_chunks_by_title(elements)

    documents = summarise_chunks(chunks)
    
    db = create_vector_store(documents)

    print("🚀 Ingestion pipeline completed")
    return db
