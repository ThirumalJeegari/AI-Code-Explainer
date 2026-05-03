import streamlit as st
from llm_helper import explain_code

st.set_page_config(page_title="AI Code Explainer", layout="wide")

st.title("🧠 AI Code Explainer Tool")
st.write("Paste your code and get step-by-step explanation")

# Inputs
language = st.selectbox(
    "Select Programming Language",
    ["Python", "Java", "JavaScript", "C++", "C", "Other"]
)

mode = st.radio(
    "Choose Explanation Mode",
    ["Beginner", "Advanced"]
)

code = st.text_area("Paste your code here", height=250)

if st.button("Explain Code"):
    if code.strip() == "":
        st.warning("Please enter some code!")
    else:
        with st.spinner("Analyzing code..."):
            result = explain_code(code, language, mode)

        st.subheader("📘 Explanation")
        st.write(result)