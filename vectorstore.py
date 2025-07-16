import os
from dotenv import load_dotenv
load_dotenv()

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain.docstore.document import Document
from langchain.embeddings import HuggingFaceEmbeddings
import google.generativeai as genai

# === 1. Configure Gemini ===
genai.configure(api_key=os.getenv("AIzaSyCUnQ1pv4O8u5Ev9meKeg2G5D7mHYQzfR8"))
model = genai.GenerativeModel(model_name="gemini-pro")

# === 2. Embeddings ===
embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# === 3. In-memory FAISS vector store ===
vector_store = None

def split_text(text):
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    chunks = splitter.split_text(text)
    return [Document(page_content=chunk) for chunk in chunks]

def build_vector_store(text):
    global vector_store
    docs = split_text(text)
    vector_store = FAISS.from_documents(docs, embedding_model)

def retrieve_relevant_chunks(text, query):
    global vector_store
    if vector_store is None:
        build_vector_store(text)
    docs = vector_store.similarity_search(query, k=3)
    return docs


