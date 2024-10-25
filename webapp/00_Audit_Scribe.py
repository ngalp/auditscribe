import streamlit as st
from webapp.logo import icon, logo

st.set_page_config(page_title="Audit Scribe", page_icon=icon, layout="wide")

# You can always call this function where ever you want
st.markdown("## 00_ – Your Audit Assistant!")

multi='''👋 Say hello to **Audit Scribe** ✏️—the friendly, always-ready virtual assistant here to supercharge your audit workflow! Whether you’re 📝 drafting emails, 🔍 clarifying policies, or 📊 summarizing findings, Audit Scribe takes the heavy lifting out of repetitive tasks.\  

With smart, AI-powered insights at your fingertips, you’ll breeze through audits with confidence and focus on what really matters—💡 driving impactful results. Just ask away, and let Audit Scribe be your go-to companion, making audits smoother, faster, and even a little more fun! 🚀\  

Your audit journey just got a whole lot easier—let’s get started! 🎉\
'''

st.markdown(multi)
