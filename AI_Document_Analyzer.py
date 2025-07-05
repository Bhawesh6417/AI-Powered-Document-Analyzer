import streamlit as st
import os
import tempfile
import google.generativeai as genai
from google.generativeai import GenerativeModel
from dotenv import load_dotenv
import pandas as pd
import docx2txt
import PyPDF2

# Load API key
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")
if API_KEY:
    genai.configure(api_key=API_KEY)

# Set page config
st.set_page_config(page_title="Gemini File Chatbot 🤖", layout="wide")
st.title("Gemini File Q&A Chatbot")
st.markdown("Upload a **PDF**, **DOCX**, **Excel**, or **CSV** file and ask questions based on its content.")

# Initialize Gemini model
model = GenerativeModel("gemini-2.0-flash-exp")

# File uploader
uploaded_file = st.file_uploader("Upload a file", type=["pdf", "docx", "xlsx", "csv"])

file_text = ""

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(uploaded_file.read())
        temp_path = tmp.name

    file_type = uploaded_file.name.split(".")[-1].lower()

    try:
        if file_type == "pdf":
            with open(temp_path, "rb") as f:
                reader = PyPDF2.PdfReader(f)
                for page in reader.pages:
                    file_text += page.extract_text()

        elif file_type == "docx":
            file_text = docx2txt.process(temp_path)

        elif file_type == "xlsx":
            df = pd.read_excel(temp_path)
            file_text = df.to_string(index=False)

        elif file_type == "csv":
            df = pd.read_csv(temp_path)
            file_text = df.to_string(index=False)

        else:
            st.warning("Unsupported file format.")

        st.success("File content successfully extracted!")

    except Exception as e:
        st.error(f"Error reading file: {e}")

# Text area for questions
if file_text:
    user_query = st.text_area("Ask a question about the file:", height=100)

    if st.button(" Get Answer"):
        with st.spinner("Thinking..."):
            try:
                prompt = f"""
You are an AI assistant. Use the content below to answer the user's question.

File Content:
"""
                prompt += file_text[:20000]  # truncate if file is too long
                prompt += f"\n\nUser's Question: {user_query}\nAnswer:"

                response = model.generate_content(prompt)
                st.subheader(" Answer")
                st.markdown(response.text)
            except Exception as e:
                st.error(f"Failed to generate answer: {e}")
else:
    st.info("Please upload a file to get started.")
