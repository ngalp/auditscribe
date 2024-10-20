import streamlit as st
from PIL import Image
import requests

url='https://github.com/ngalp/auditscribe/blob/main/images/logo.png?raw=true'
response = requests.get(url)
img = Image.open(requests.get(url, stream=True).raw)

st.logo(img,link='https://auditscribe.streamlit.app/', icon_image=img)

st.text('Fixed width text')

import base64
import streamlit as st


@st.cache(allow_output_mutation=True)
def get_base64_of_bin_file(png_file):
    with open(png_file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


def build_markup_for_logo(
    png_file,
    background_position="50% 10%",
    margin_top="10%",
    image_width="60%",
    image_height="",
):
    binary_string = get_base64_of_bin_file(png_file)
    return """
            <style>
                [data-testid="stSidebarNav"] {
                    background-image: url("data:image/png;base64,%s");
                    background-repeat: no-repeat;
                    background-position: %s;
                    margin-top: %s;
                    background-size: %s %s;
                }
            </style>
            """ % (
        binary_string,
        background_position,
        margin_top,
        image_width,
        image_height,
    )


def add_logo(png_file):
    logo_markup = build_markup_for_logo(png_file)
    st.markdown(
        logo_markup,
        unsafe_allow_html=True,
    )

add_logo(img)

st.markdown("# Home")