import fitz  # PyMuPDF

def parse_document(file):
    if file.name.endswith(".pdf"):
        text = ""
        with fitz.open(stream=file.read(), filetype="pdf") as doc:
            for page in doc:
                text += page.get_text()
        return text
    elif file.name.endswith(".txt"):
        return file.read().decode("utf-8")
    return ""
