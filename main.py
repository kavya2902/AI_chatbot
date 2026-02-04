from fastapi import FastAPI
from pydantic import BaseModel

from vector_db import search_data
from llm import ask_llm

app = FastAPI()


class Query(BaseModel):
    question: str


@app.post("/chat")
def chat(query: Query):

    result = search_data(query.question)

    context = ""

    for match in result["matches"]:
        context += match["metadata"]["text"] + "\n"

    prompt = f"""
Use this info to answer:

{context}

Question:
{query.question}
"""

    answer = ask_llm(prompt)

    return {"answer": answer}
