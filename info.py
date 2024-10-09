import streamlit as st
with st.sidebar:
    with st.echo():
        st.write("Audit Scribe")

LOGO_URL_LARGE="https://github.com/ngalp/auditscribe/blob/main/images/logo.png?raw=true"
LOGO_URL_SMALL="https://github.com/ngalp/auditscribe/blob/main/images/logo.png?raw=true"
st.logo(
    LOGO_URL_LARGE,
    link="https://auditscribe.streamlit.app/",
    icon_image=LOGO_URL_SMALL, width=100
)