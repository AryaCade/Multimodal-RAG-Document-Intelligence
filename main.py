from pipeline import run_ingestion_pipeline
from rag.answer_generator import generate_final_answer

db = run_ingestion_pipeline("./docs/Attention_is_all_you_need.pdf")

query = "What are the advantages of self-attention layers?"
retriever = db.as_retriever(search_kwargs={"k": 3})
chunks = retriever.invoke(query)

answer = generate_final_answer(chunks, query)
print(answer)
