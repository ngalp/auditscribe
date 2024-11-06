####################
# the first section is adapted from https://github.com/mmz-001/knowledge_gpt/blob/main/knowledge_gpt/main.py
####################

import streamlit as st
from openai import OpenAI

st.title("📝 Chat With Your Documents")

EMBEDDING = "openai"
VECTOR_STORE = "faiss"
MODEL_LIST = ["gpt-3.5-turbo", "gpt-4"]


with st.sidebar:
    openai_api_key = st.text_input(label = ":key: OpenAI API Key:", key="file_qa_api_key", help="OpenAI API Key required for chat completion. Key will not be stored.",type="password",placeholder="Paste your OpenAI API key here")

    if not openai_api_key:
        st.warning(
            "Enter your OpenAI API key in the sidebar. You can get a key at"
            " https://platform.openai.com/account/api-keys."
        )

    model: str = st.selectbox("Model", options=MODEL_LIST)  

    with st.expander("Advanced Options"):
        return_all_chunks = st.checkbox("Show all chunks retrieved from vector search")
        show_full_doc = st.checkbox("Show parsed contents of the document")
        

uploaded_file = st.file_uploader("Upload a pdf, docx, or txt file", type=["pdf", "docx", "txt"])

question = st.text_input(
    ":eyes: What would you like to know?",
    placeholder="Can you give me a short summary?",
    disabled=not uploaded_file,
)

if uploaded_file and question and openai_api_key:
    # Create an OpenAI client.
    client = OpenAI(api_key=openai_api_key)

    # Process the uploaded file and question.
    document = uploaded_file.read().decode()
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