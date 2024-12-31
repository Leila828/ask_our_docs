```markdown
# AI Call Center Application

## Overview
This project is a Streamlit-based application that allows users to upload PDF documents, process their content, and perform question-answering using a retrieval-based model powered by HuggingFace.

## Features
- Upload and process multiple PDF documents.
- Split text into manageable chunks for efficient querying.
- Leverage HuggingFace embeddings and a language model for question-answering.
- Simple and user-friendly Streamlit interface.

## Requirements
- Python 3.8+
- HuggingFace API Token

## Installation
1. Clone the repository.
2. Create a virtual environment:
    ```bash
    py -m venv venv
    source venv/bin/activate # On Windows: venv\Scripts\activate
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Create a `.env` file and add your HuggingFace API token:
    ```
    HUGGINGFACEHUB_API_TOKEN=<your_huggingface_api_token>
    ```

## Usage
Run the application:
```bash
streamlit run app/main.py
```

## Folder Structure
- `app/main.py`: Main application logic.
- `app/utils.py`: Utility functions for file processing and environment setup.
- `app/qa_chain.py`: Logic for setting up the RetrievalQA chain.
- `requirements.txt`: Required Python dependencies.
- `.env`: Environment variables.
- `README.md`: Project overview and usage instructions.

## Contributing
Feel free to submit issues or pull requests to enhance this project.