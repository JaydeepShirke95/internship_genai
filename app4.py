import streamlit as st
import google.generativeai as genai

st.title("Google Gemini Integration with Streamlit")
user_input = st.text_input("Enter your prompt for Google Gemini:")

genai.configure(api_key="AIzaSyAt4DUHeQNR0CmLoAuM0fZM6IaxoKmyggc")

model = genai.GenerativeModel("models/gemini-2.5-flash")

if user_input:
    response = model.generate_content(user_input)
    st.write("response",  response.text)