import streamlit as st
from PIL import Image
import requests
from io import BytesIO  
import random  
import hmac  

st.set_page_config(page_title="✏️ Audit Scribe", layout="wide")
#st.set_page_config(page_title="Audit Scribe",  layout="wide")

#logo =Image.open(BytesIO(requests.get('https://github.com/ngalp/auditscribe/blob/main/webapp/logo/logo.ico?raw=true').content))
#icon =Image.open(BytesIO(requests.get('https://github.com/ngalp/auditscribe/blob/main/webapp/logo/icon.ico?raw=true').content)) 
#st.logo(logo,  link='https://auditscribe.streamlit.app', icon_image=icon)

# You can always call this function where ever you want
st.markdown("## ✏️ Audit Scribe – Your Audit Assistant!")

multi='''👋 Say hello to **Audit Scribe** ✏️—the friendly, always-ready virtual assistant here to supercharge your audit workflow! Whether you’re 📝 drafting emails, 🔍 clarifying policies, or 📊 summarizing findings, Audit Scribe takes the heavy lifting out of repetitive tasks. 

With smart, AI-powered insights at your fingertips, you’ll breeze through audits with confidence and focus on what really matters—💡 driving impactful results. Just ask away, and let Audit Scribe be your go-to companion, making audits smoother, faster, and even a little more fun! 🚀

Your audit journey just got a whole lot easier—click on the side bar options to get started! 🎉

* Chat With Your Documents
* Chat with Your Data
* Visualise Your Data
'''

st.markdown(multi)

#You may use "st.expander" so the disclaimer can be collapsed or expanded.

multi_notice="""

This web application is developed as a proof-of-concept prototype. The information provided here is NOT intended for actual usage and should not be relied upon for making any decisions, especially those related to financial, legal, or healthcare matters.

Furthermore, please be aware that the LLM may generate inaccurate or incorrect information. You assume full responsibility for how you use any generated output.

Always consult with qualified professionals for accurate and personalized advice.

"""
  
def check_password():  
    """Returns `True` if the user had the correct password."""  
    def password_entered():  
        """Checks whether a password entered by the user is correct."""  
        if hmac.compare_digest(st.session_state["password"], st.secrets["password"]):  
            st.session_state["password_correct"] = True  
            del st.session_state["password"]  # Don't store the password.  
        else:  
            st.session_state["password_correct"] = False  
    # Return True if the passward is validated.  
    if st.session_state.get("password_correct", False):  
        return True  
    # Show input for password.  
    st.text_input(  
        "Please enter password below:", type="password", on_change=password_entered, key="password"  
    )  
    if "password_correct" in st.session_state:  
        st.error("😕 Password incorrect. Please try again.")  
    return False

if not check_password():  
    st.stop()

with st.expander("IMPORTANT NOTICE"):
    st.write(multi_notice)