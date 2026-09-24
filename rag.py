import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

PDF_File = "data/nutrition.pdf"
HF_TOKEN = os.getenv("HF_TOKEN")

def Create_Rag():
    if not os.path.exists(PDF_File):
        raise FileNotFoundError("File Not Found")
    else:
        document = PyPDFLoader(PDF_File).load()
        splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        chunks = splitter.split_documents(document)
        
        embedding = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2",
            model_kwargs={'token': HF_TOKEN}
        )
        
        db = FAISS.from_documents(chunks, embedding)
        db.save_local("data")
        return len(chunks)

def load_rag():
    embedding = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        model_kwargs={'token': HF_TOKEN}
    )
    db = FAISS.load_local("data", embedding, allow_dangerous_deserialization=True)
    return db

