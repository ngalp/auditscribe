#################################################################################
# the section is adapted (not direct copy) from https://github.com/frog-land/Chat2VIS_Streamlit/blob/main/Chat2VIS.py
#################################################################################

import pandas as pd
from openai import OpenAI
import requests
import streamlit as st
import warnings
from utility import check_password

st.title("📊 Chat With Your Documents and Data")

MODEL_LIST = ["gpt-3.5-turbo", "gpt-4"]

# List to hold documents
documents = {}
documents["Transport_Policy"] =  requests.get('https://raw.githubusercontent.com/ngalp/auditscribe/refs/heads/main/webapp/documents/Transport_Policy.txt').text

# List to hold datasets
datasets = {}
datasets["Transport"] = pd.read_csv("https://raw.githubusercontent.com/ngalp/auditscribe/refs/heads/main/webapp/data/Transport_Claims.csv")

with st.sidebar:
    if not check_password():  
        st.warning(
                "Enter the app password to continue."
            )
        st.stop()  

    openai_api_key = st.text_input(label = ":key: OpenAI API Key:", key="openai_api_key", help="OpenAI API Key required for chat completion. Key will not be stored.",type="password",placeholder="Paste your OpenAI API key here")

    if not openai_api_key:
        st.warning(
            "Enter your OpenAI API key in the sidebar. You can get a key at"
            " https://platform.openai.com/account/api-keys."
        )
    # First we want to choose the dataset, but we will fill it with choices once we've loaded one
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

    dataset_container = st.empty()
    # Add facility to upload a dataset
    try:
        uploaded_file = st.file_uploader(":computer: Load a CSV file:", type="csv")
        index_no=0
        if uploaded_file:
            # Read in the data, add it to the list of available datasets. Give it a nice name.
            file_name = "Data"
            datasets[file_name] = pd.read_csv(uploaded_file)
            # We want to default the radio button to the newly added dataset
            index_no = len(datasets)-1
    except Exception as e:
        st.error("File failed to load. Please select a valid CSV file.")
        print("File failed to load.\n" + str(e))
    # Radio buttons for dataset choice
    chosen_dataset = dataset_container.radio(":bar_chart: Choose your data:",datasets.keys(),index=index_no)#,horizontal=True,)

    # Check boxes for model choice
    st.write(":brain: Choose your model(s):")
    # Keep a dictionary of whether models are selected or not
    model: str = st.selectbox("Model", options=MODEL_LIST)  

 # Text area for query
question = st.text_area(":eyes: What would you like to know?",
                        placeholder="Based on the dataset, identify the top claimant and draft an email to him to sample check quoting the transport claim policy.",
                        height=10)
go_btn = st.button("Go...")

if question and openai_api_key:
    # Create an OpenAI client
    client = OpenAI(api_key=openai_api_key)
    document = documents[chosen_documents]
    data_string = datasets[chosen_dataset].to_csv(header=None, index=False).strip('\n').split('\n')
    data_desc = "The dataframe has columns '" \
            + "','".join(str(x) for x in datasets[chosen_dataset].columns) + "'. "
    for i in datasets[chosen_dataset].columns:
        if len(datasets[chosen_dataset][i].drop_duplicates()) < 20 and datasets[chosen_dataset].dtypes[i]=="O":
            data_desc = data_desc + "\nThe column '" + i + "' has categorical values '" + \
                "','".join(str(x) for x in datasets[chosen_dataset][i].drop_duplicates()) + "'. "
        elif datasets[chosen_dataset].dtypes[i]=="int64" or datasets[chosen_dataset].dtypes[i]=="float64":
            data_desc = data_desc + "\nThe column '" + i + "' is type " + str(datasets[chosen_dataset].dtypes[i]) + " and contains numeric values. "   
 
    dataqa_prompt = "Given the document and dataframe, answer the following question:"
    messages = [
        {
            "role": "user",
            "content": f"{dataqa_prompt} \n\n---\n\n Question: {question}  \n\n---\n\n Document: {document} \n\n---\n\n Dataframe description: {data_desc} \n\n---\n\n \n\n---\n\n Dataframe: {data_string}  ",
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
        

    # Display the datasets in a list of tabs
    # Create the tabs
tab_list = st.tabs(datasets.keys())

# Load up each tab with a dataset
for dataset_num, tab in enumerate(tab_list):
    with tab:
        # Can't get the name of the tab! Can't index key list. So convert to list and index
        dataset_name = list(datasets.keys())[dataset_num]
        st.subheader(dataset_name)
        st.write(datasets[dataset_name])


# Insert footer to reference dataset origin  
footer="""<style>.footer {position: fixed;left: 0;bottom: 0;width: 100%;text-align: center;}</style><div class="footer">
<p> <a style='display: block; text-align: center;'> Synthetic Datasets </a></p></div>"""
st.caption("Synthetic Datasets")

# Hide menu and footer
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)