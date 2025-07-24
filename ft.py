# ft.py
import streamlit as st
from CB_Model import HealthChatbot

@st.cache_resource
def load_chatbot():
    return HealthChatbot()

def main():
    st.title("Medical Diagnosis Chatbot")
    st.write("Ask general health questions (not for emergencies)")
    
    chatbot = load_chatbot()
    user_input = st.text_input("Your health question:")
    
    if user_input:
        with st.spinner("Analyzing..."):
            response = chatbot.get_response(user_input)
        st.text_area("Response:", value=response, height=200)

if __name__ == "__main__":
    main()