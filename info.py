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
st.set_page_config(page_title="HDB Kaki", page_icon=img, layout="wide")

st.image(img, width=500)

st.markdown("## ✏️ Meet Audit Scribe – Your Audit Sidekick!")

st.markdown(
    "👋 Say hello to **Audit Scribe** ✏️—the friendly, always-ready virtual assistant here to supercharge your audit workflow! Whether you’re 📝 drafting emails, 🔍 clarifying policies, or 📊 summarizing findings, Audit Scribe takes the heavy lifting out of repetitive tasks.  

With smart, AI-powered insights at your fingertips, you’ll breeze through audits with confidence and focus on what really matters—💡 driving impactful results. Just ask away, and let Audit Scribe be your go-to companion, making audits smoother, faster, and even a little more fun! 🚀  

Your audit journey just got a whole lot easier—let’s get started! 🎉
")

