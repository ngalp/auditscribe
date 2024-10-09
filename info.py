import streamlit as st
from openai import OpenAI

image = Image.open('/path/image.png')
st.sidebar.image(image, use_column_width=False)