import streamlit as st
import requests

API_URL = "http://localhost:5000/review"

st.title("Code Review Assistant 🧠💻")

uploaded = st.file_uploader("Upload source code file")

if uploaded:
    st.write("Reviewing your code... please wait ⏳")

    files = {"file": (uploaded.name, uploaded.getvalue())}

    response = requests.post(API_URL, files=files)

    if response.status_code == 200:
        data = response.json()
        st.success("Review Completed ✔")
        st.subheader("Report:")
        st.write(data["report"])
    else:
        st.error("Error: " + response.text)
