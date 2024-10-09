import streamlit as st
from PIL import Image
import requests

url='https://github.com/ngalp/auditscribe/blob/main/images/logo.png?raw=true'
response = requests.get(url)
img = Image.open(requests.get(url, stream=True).raw)

st.logo(img,link='https://auditscribe.streamlit.app/', icon_image=img)