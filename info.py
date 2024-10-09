import streamlit as st
from PIL import Image
import requests
from io import BytesIO
from streamlit_extras.app_logo import add_logo

url='https://github.com/ngalp/auditscribe/blob/main/images/logo.png?raw=true'
response = requests.get(url)
img = Image.open(requests.get(url, stream=True).raw)

with st.sidebar:
    with st.echo():
        st.write("Audit Scribe")

st.sidebar.image(img, use_column_width=True)
st.sidebar.markdown("AUDIT SCRIBE")

def example():
    if st.checkbox("Use url", value=True):
        add_logo("http://placekitten.com/120/120")
    else:
        add_logo("gallery/kitty.jpeg", height=300)
    st.write("👈 Check out the cat in the nav-bar!")