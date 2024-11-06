import streamlit as st
from PIL import Image
import requests
from io import BytesIO  
from utility import check_password

st.set_page_config(page_title="✏️ Audit Scribe - Methodology", layout="wide")


st.markdown("## ✏️ Audit Scribe – Your Audit Assistant!")

multi='''## Methodology: Using Large Language Models (LLMs) to "Chat" with Documents and Data

(Start)  
    |  
    v  
(Enter Password)  
    |  
    v  
[Is password correct?] -- No --> (Display Error & Retry) --> (Enter Password)  
    |  
   Yes  
    v  
(Enter OpenAI API Key)  
    |  
    v  
[Is API key valid?] -- No --> (Display Error & Retry) --> (Enter OpenAI API Key)  
    |  
   Yes  
    v  
(Select/Attach Document)  
    |  
    v  
[Is document selected?]   
    |  
   Yes  
    v  
(Select/Attach Data)  
    |  
    v  
[Is data selected?]   
    |  
   Yes  
    v  
(Key in Question)  
    |  
    v  
(Wait for Response)  
    |  
    v  
(Display Response)  
    |  
    v  
(End)  


### Introduction

Large Language Models (LLMs) like GPT-4 have revolutionized how we interact with documents, data, and text-based content. By leveraging the conversational capabilities of LLMs, organizations can streamline processes such as document analysis, data extraction, and decision-making support. This methodology outlines how LLMs can be employed to "chat" with documents and structured data, making them powerful tools for tasks such as summarization, answering queries, extracting insights, and identifying patterns.

### Key Components

### 1. **Document Understanding**
LLMs can read, understand, and interpret a wide range of document formats, including PDFs, text documents. By analyzing the content, LLMs can be used to:
- **Summarize Text**: LLMs can condense long documents into concise summaries, extracting the most important details.
- **Answer Questions**: Users can "ask" specific questions about a document, and the LLM can identify relevant sections of text to generate accurate responses.
- **Identify Key Themes**: Through natural language processing, LLMs can identify and extract themes, topics, or sentiments present in a document.

This is achieved in the "Chat With Your Documents" Functionality.

### 2. **Data Interpretation**
For structured data (e.g., spreadsheets), LLMs can assist in analyzing and deriving insights. Tasks include:
- **Data Extraction**: LLMs can pull out specific data points from large datasets, such as extracting financial data or identifying key metrics from reports.
- **Data Analysis**: LLMs can be used to interpret data trends, perform calculations, and answer complex queries based on structured data inputs.
- **Visualization Suggestions**: LLMs can also suggest appropriate data visualizations (e.g., charts, graphs) based on the data and the questions posed.

This is achieved in the "Chat With Your Data" and "Visualize Your Data" Functionality.

### 3. **Conversational Interface**
The core feature of using an LLM with documents and data is its ability to engage in a conversational manner:
- **Query-Response Interaction**: Users can interact with the LLM by asking it specific questions about the document or dataset. The LLM understands the context and can answer based on the content provided.
- **Follow-up Dialogue**: The conversational model allows for iterative questioning, where users can ask follow-up questions or request clarifications, enabling deeper exploration of the data or document.

## Use Cases

### 1. **Legal Document Review**
LLMs can "chat" with policy documents to:
- **Extract Key Clauses**: Identify important terms, conditions, and clauses within policies.
- **Summarize Text**: Provide a summary of a long policy document, highlighting relevant points.
- **Answer Policy Queries**: Answer specific questions based on the content of the policy text, such as in the context of specific policy violations.

### 2. **Financial Data Analysis**
For audit teams, LLMs can:
- **Analyze Financial Data**: "Chat" with financial reports to identify trends, anomalies, or specific metrics like high risk transactions.
- **Generate Reports**: Automatically generate financial summaries or interpret the health based on the provided data.

### Conclusion

By integrating LLMs into document and data management processes, organizations can achieve greater efficiency, improved accuracy, and enhanced decision-making capabilities. The ability to "chat" with data and documents brings a new level of interactivity, enabling users to ask questions, generate insights, and interact with large datasets in a more intuitive and automated way.

### Follow-Up Actions

The current application has showcased functionalities to Chat With Documents and Datasets. Greater customization is required to incorporate agents which can identify the appropriate actions based on user queries and carry them our more effectively.
'''

st.markdown(multi)

