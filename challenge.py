from backend.vectorstore import get_llm_response

def generate_challenges(text):
    prompt = f"Generate 3 logic or comprehension-based questions from the following document:\n\n{text[:3000]}"
    questions = get_llm_response(prompt)
    return questions.strip().split("\n")[:3]

def evaluate_response(text, questions, answers):
    results = []
    for q, a in zip(questions, answers):
        prompt = f"""
Document: {text[:3000]}
Question: {q}
User's Answer: {a}

Evaluate the user's answer, provide feedback, and cite support from the document.
"""
        feedback = get_llm_response(prompt)
        results.append((feedback, "Referenced from top context"))
    return results
