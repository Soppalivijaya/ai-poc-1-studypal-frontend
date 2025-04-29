import streamlit as st
import requests

st.set_page_config(
    page_title = "StudyPal",
    page_icon = "🤖",
    layout = "centered",
)

st.title("StudyPal Application")

app_url = "http://127.0.0.1:8000/ask"

# Get User Input

user_question = st.text_input(label="Ask Your question", placeholder="Ex. What is AI")

#button to trigger backend API

if st.button("Get Answer"):
    response = requests.post(
        url = app_url,
        json = {"question": user_question},
    )

    result = response.json()
    answer = result["answer"]

    st.success(answer)