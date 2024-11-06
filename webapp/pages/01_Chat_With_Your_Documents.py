####################
# the section is adapted (not direct copy) from https://github.com/mmz-001/knowledge_gpt/blob/main/knowledge_gpt/main.py
####################

import streamlit as st
from openai import OpenAI
from utility import check_password
import requests


st.title("📝 Chat With Your Documents")

EMBEDDING = "openai"
VECTOR_STORE = "faiss"
MODEL_LIST = ["gpt-3.5-turbo", "gpt-4"]

# List to hold documents
documents = {}
documents["Transport_Policy"] =  requests.get('https://raw.githubusercontent.com/ngalp/auditscribe/refs/heads/main/webapp/documents/Transport_Policy.txt').text

with st.sidebar:
    if not check_password():  
        st.warning(
                "Enter the app password to continue."
            )
        st.stop()  

    openai_api_key = st.text_input(label = ":key: OpenAI API Key:", key="file_qa_api_key", help="OpenAI API Key required for chat completion. Key will not be stored.",type="password",placeholder="Paste your OpenAI API key here")

    if not openai_api_key:
        st.warning(
            "Enter your OpenAI API key in the sidebar. You can get a key at"
            " https://platform.openai.com/account/api-keys."
        )

    model: str = st.selectbox("Model", options=MODEL_LIST)  

    documents_container = st.empty()
    # Add facility to upload a dataset
    try:
        uploaded_file = st.file_uploader("Upload a pdf, docx, or txt file", type=["pdf", "docx", "txt"])
        index_no=0
        if uploaded_file:
            # Read in the document, add it to the list of available document. 
            file_name = "Document"
            documents[file_name] = uploaded_file.read().decode()
            # We want to default the radio button to the newly added dataset
            index_no = len(documents)-1
    except Exception as e:
        st.error("File failed to load. Please select a valid CSV file.")
        print("File failed to load.\n" + str(e))
    # Radio buttons for documents choice
    chosen_documents = documents_container.radio(":memo: Choose your data:",documents.keys(),index=index_no)#,horizontal=True,)

    
question = st.text_input(
    ":eyes: What would you like to know?",
    placeholder="Can you give me a short summary?"
)

if question and openai_api_key:
    # Create an OpenAI client.
    client = OpenAI(api_key=openai_api_key)

    # Process the uploaded file and question.
    document = documents[chosen_documents]
    messages = [
        {
            "role": "user",
            "content": f"Here's a document: {document} \n\n---\n\n {question}",
        }
        ]

    # Generate an answer using the OpenAI API.
    stream = client.chat.completions.create(
        model=model,
        messages=messages,
        stream=True,
        )

    # Stream the response to the app using `st.write_stream`.
    st.write_stream(stream)