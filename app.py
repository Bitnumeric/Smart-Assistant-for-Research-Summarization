import streamlit as st
from backend.parser import parse_document
from backend.summarizer import generate_summary
from backend.qa import answer_question
from backend.challenge import generate_challenges, evaluate_response

st.set_page_config(page_title="Smart GenAI Assistant", layout="wide")
st.title("📄 Smart Assistant for Research Summarization")

uploaded_file = st.file_uploader("Upload a PDF or TXT file", type=["pdf", "txt"])

if uploaded_file:
    doc_text = parse_document(uploaded_file)
    summary = generate_summary(doc_text)
    st.subheader("🔍 Document Summary")
    st.write(summary)
    
    mode = st.radio("Select Mode:", ["Ask Anything", "Challenge Me"])
    
    if mode == "Ask Anything":
        question = st.text_input("Ask your question:")
        if question:
            answer, justification = answer_question(doc_text, question)
            st.markdown(f"**Answer:** {answer}")
            st.markdown(f"_Justification:_ {justification}")
            
    elif mode == "Challenge Me":
        st.subheader("Answer These Questions:")
        questions = generate_challenges(doc_text)
        user_answers = []
        for idx, q in enumerate(questions):
            ans = st.text_input(f"Q{idx+1}: {q}")
            user_answers.append(ans)
        
        if st.button("Submit Answers"):
            results = evaluate_response(doc_text, questions, user_answers)
            for i, (feedback, ref) in enumerate(results):
                st.markdown(f"**Q{i+1} Feedback:** {feedback}")
                st.markdown(f"_Reference:_ {ref}")
