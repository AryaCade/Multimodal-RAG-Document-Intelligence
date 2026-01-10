import json
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from config import ANSWER_MODEL

def generate_final_answer(chunks, query):
    llm = ChatGoogleGenerativeAI(model=ANSWER_MODEL, temperature=0)

    prompt = f"""
    You are a question-answering assistant.

    QUESTION:
    {query}

    Use ONLY the information from the documents below.
    If the answer is not present, say:
    "I don't have enough information to answer that question based on the provided documents."

    DOCUMENTS:
"""

    for i, chunk in enumerate(chunks):
        data = json.loads(chunk.metadata["original_content"])
        prompt += f"--- Document {i+1} ---\n{data.get('raw_text','')}\n\n"

    message = HumanMessage(content=[{"type": "text", "text": prompt}])
    response = llm.invoke([message])
    return response.content
