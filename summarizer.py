from transformers import pipeline

# Load the local summarization model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def generate_summary(doc_text):
    # Limit input to 1024 tokens
    doc_text = doc_text[:1024]
    result = summarizer(doc_text, max_length=150, min_length=40, do_sample=False)
    return result[0]['summary_text']
