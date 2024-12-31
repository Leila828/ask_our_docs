import streamlit as st
from dotenv import load_dotenv
from utils import initialize_environment, process_uploaded_files
from qa_chain import create_qa_chain

def main():
    """Main application logic."""
    # Load environment and API token
    huggingface_api_token = initialize_environment()

    # Configure Streamlit app
    st.set_page_config(page_title="AI Call Center")
    st.header(" Explore Your Data with One Click")

    # File upload
    uploaded_files = st.file_uploader("Upload Your Company PDFs", type="pdf", accept_multiple_files=True)

    if uploaded_files:
        st.info("Processing your uploaded documents. This might take a while...")

        # Process files and extract text
        all_text = process_uploaded_files(uploaded_files)

        # Create QA chain
        qa_chain = create_qa_chain(all_text, huggingface_api_token)

        # Get user query
        client_question = st.text_input("Ask a question:")
        if client_question:
            with st.spinner("Finding the best answer..."):
                try:
                    answer = qa_chain.run(client_question)
                    # Clean up the response to extract the actual answer
                    cleaned_response = answer['answer'] if isinstance(answer,
                                                                      dict) and 'answer' in answer else answer
                    cleaned_response = cleaned_response.strip().split("Answer:")[-1].strip()
                    st.write("Answer:", cleaned_response)
                except Exception as e:
                    st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
