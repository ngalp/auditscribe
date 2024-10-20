import streamlit as st
from PIL import Image
import requests

url='https://github.com/ngalp/auditscribe/blob/main/images/logo.png?raw=true'
response = requests.get(url)
img = Image.open(requests.get(url, stream=True).raw)

#st.logo(img,link='https://auditscribe.streamlit.app/', icon_image=img)

st.text('Fixed width text')

from PIL import Image
import streamlit as st

# You can always call this function where ever you want

def add_logo(logo_path, width, height):
    """Read and return a resized logo"""
    logo = Image.open(requests.get(url, stream=True).raw)
    modified_logo = logo.resize((width, height))
    return modified_logo

my_logo = add_logo(logo_path=url, width=50, height=60)
st.sidebar.image(my_logo)

# OR

# st.sidebar.image(add_logo(logo_path="your/logo/path", width=50, height=60)) 