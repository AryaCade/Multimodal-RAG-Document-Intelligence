from dotenv import load_dotenv
load_dotenv()

PDF_STRATEGY = "hi_res"
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

SUMMARY_MODEL = "gemini-2.5-flash"
ANSWER_MODEL = "gemini-2.5-flash"

CHROMA_DIR = "db/chroma_db"
