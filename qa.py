from backend.vectorstore import retrieve_relevant_chunks, get_llm_response

def answer_question(text, question):
    context = retrieve_relevant_chunks(text, question)
    prompt = f"""
Use the context below to answer the question.
Context:
{context}

Question:
{question}

Answer the question and cite the paragraph or section it comes from.
"""
    response = get_llm_response(prompt)
    # Optionally split response to get answer and justification
    return response, "Based on top retrieved context."
