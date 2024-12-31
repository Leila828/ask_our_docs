import os
import tempfile
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
import streamlit as st

def initialize_environment():
    """Load environment variables."""
    load_dotenv()
    huggingface_api_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")
    if not huggingface_api_token:
        st.error("HuggingFace API token not found. Please set it in the environment variables.")
        st.stop()
    return huggingface_api_token

def process_uploaded_files(uploaded_files):
    """Extract text content from uploaded PDF files."""
    all_text = ""
    for uploaded_file in uploaded_files:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
            temp_file.write(uploaded_file.read())
            temp_file_path = temp_file.name

        loader = PyPDFLoader(temp_file_path)
        documents = loader.load()
        all_text += "\n".join([doc.page_content for doc in documents])

    return all_text