import streamlit as st
from PIL import Image
import requests
from io import BytesIO

url='https://github.com/ngalp/auditscribe/blob/main/images/logo.png?raw=true'
response = requests.get(url)
img = Image.open(requests.get(url, stream=True).raw)

with st.sidebar:
    with st.echo():
        st.write("Audit Scribe")

st.sidebar.image(img, use_column_width=True)
st.sidebar.markdown("AUDIT SCRIBE")