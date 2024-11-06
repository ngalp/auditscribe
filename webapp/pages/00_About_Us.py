import streamlit as st
from PIL import Image
import requests
from io import BytesIO  
from utility import check_password

st.set_page_config(page_title="✏️ Audit Scribe - About Us", layout="wide")

# You can always call this function where ever you want
st.markdown("## ✏️ Audit Scribe – Your Audit Assistant!")

multi='''## Problem Statement

Auditors spend a significant amount of time (1-2 hours daily) drafting and sending emails to address audit anomalies, request information, and reference policies. This manual process detracts from higher-value tasks like data analysis, risk assessments, and document reviews. It also increases the risk of human error, potentially leading to missed anomalies or incomplete responses. With about 50 auditors impacted, this inefficiency represents a significant productivity loss and potential audit inaccuracies. 

**Key Question:** How can the email drafting process be streamlined to save time and improve accuracy, while allowing auditors to maintain control over the final communications?

## Proposed Solution

**Audit Scribe** is an AI-powered tool designed to automate the email drafting process. By using Large Language Models (LLMs), Audit Scribe generates first drafts of emails that address audit anomalies, reference relevant policies, and suggest appropriate tone and style adjustments based on the anomaly's severity. Auditors will review and refine the drafts to ensure accuracy and maintain control over the final communication.

**Why Not Manual Templates?**  
Manual templates lack the flexibility to adapt to varying contexts in audit communications. They are rigid, require manual adjustments, and increase the risk of inefficiency and errors.

## Impact

- **Efficiency Gains:** Reduces email drafting time from 1-2 hours daily to 15-30 minutes for review and approval.
- **Improved Accuracy:** Ensures consistency, reduces human error, and enhances the quality of communication through automatic policy referencing and customizable tone based on anomaly severity.

## Project Sponsors & Users

Audit Scribe aligns with the organization's goals of increasing operational efficiency and reducing costs. Initially, 50 auditors will benefit, but the tool has potential for broader use across other departments in compliance, risk management, and auditing.

## Data Classification & Sensitivity

- **Restricted / Sensitive**: Normal.
'''

st.markdown(multi)