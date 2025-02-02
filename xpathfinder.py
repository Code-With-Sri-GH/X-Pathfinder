# imports
import streamlit as st
import google.generativeai as genai
from prompts import locator_agent

# page config
st.set_page_config(layout='wide', page_title='XPath Finder', page_icon='🧭')

# session variables
if "response" not in st.session_state:
    st.session_state.response = None

# Hero Section
st.markdown(
    """
    <a href="https://www.youtube.com/@code-with-sri?sub_confirmation=1" target="_blank" style="text-decoration:none; font-size:24px; font-weight:bold; color:inherit;">
        <h1>Code With Sri | 🧭 X-Pathfinder </h1>
    </a>
    """, unsafe_allow_html=True
)
st.write('Your Personalized XPath Finder using AI')

input_API_KEY = st.text_input('Google Gemini API Key', placeholder='Your Personal API Key')
if input_API_KEY:
    st.success('API Key successfully set!', icon='✅')
st.html('<hr>')

# Configure the API key
genai.configure(api_key=input_API_KEY)

# Model setup
model_list = ['gemini-1.5-flash', 'gemini-1.5-pro', 'gemini-2.0-flash-exp']
model = genai.GenerativeModel(
    model_name=model_list[2], 
    system_instruction="You are an AI locator generation assistant designed to help automate the process of creating precise and unique locators for automation testing."
)


# layout
# st.title('XPath Finder 🧭 | AI Locator Finder')
# st.write('Generate unique and precise locators for Automation Testing')

application_dom = st.text_area('Application DOM', placeholder='Enter the DOM of the Application..', height=200)

description_of_locator = st.text_input('Description of locator', placeholder="Enter description of locator you're looking for")

user_input = f"""
{locator_agent}

User says:
Get me locator from this DOM: {application_dom}
Description of locator: {description_of_locator}
xpath only
"""

# Find locator
if st.button('Find Locator'):
    with st.spinner('Finding Locator...'):
        st.session_state.response = model.generate_content([user_input])

# display locator
if st.session_state.response is not None:
    st.markdown(st.session_state.response.text, unsafe_allow_html=True)