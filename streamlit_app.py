# streamlit_app.py
import streamlit as st
import requests

st.title("Chatbot")

user_input = st.text_input("Your Message:")

if user_input:
    response = requests.post("http://127.0.0.1:8000/chat/", data={"message": user_input})
    if response.status_code == 200:
        chatbot_response = response.json()['response']
        st.write(f"Chatbot Response: {chatbot_response}")
