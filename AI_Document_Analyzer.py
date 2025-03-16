import pdfplumber
import pandas as pd
import streamlit as st
import google.generativeai as genai

# API Keys
GEMINI_API_KEY = "AIzaSyB8ElKvrPTYaV9kG2q4AsTXYCc6fTIk0Uo"
genai.configure(api_key=GEMINI_API_KEY) # type: ignore
model = genai.GenerativeModel("gemini-2.0-flash-exp") # type: ignore


# Function to extract text from PDF
def extract_text_from_pdf(pdf_file):
    with pdfplumber.open(pdf_file) as pdf:
        text = "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()])
    return text

# Function to read different file types
def extract_data(file, file_type):
    if file_type == "pdf":
        return extract_text_from_pdf(file)
    elif file_type == "xlsx":
        df = pd.read_excel(file)
        return df.to_csv(index=False)  # Convert Excel to CSV-like text
    elif file_type == "csv":
        df = pd.read_csv(file)
        return df.to_csv(index=False)
    elif file_type == "txt":
        return file.read().decode("utf-8")
    return "Unsupported file type"

# Function to query Gemini AI (Updated)
def query_gemini_ai(query, document_content):
    try:
        prompt = f"Analyze the following document and answer: {query}\n\nDocument Content:\n{document_content}"
        response = model.generate_content([prompt])  # Use a list format as per the latest API
        return response.text
    except Exception as e:
        return f"Error processing query: {str(e)}"

# Streamlit UI
st.set_page_config(page_title="Document Analyzer", layout="wide")
st.title("📄 AI-Powered Document Analyzer")

# File uploader
uploaded_file = st.file_uploader("Upload a document (PDF, CSV, Excel, TXT)", type=["pdf", "csv", "xlsx", "txt"])

if uploaded_file is not None:
    # Determine file type
    file_ext = uploaded_file.name.split(".")[-1].lower()

    # Extract content
    extracted_content = extract_data(uploaded_file, file_ext)

    # Display extracted content
    st.subheader("Extracted Content:")
    st.text_area("Text from Document:", extracted_content, height=200)

    # AI Query Section
    st.subheader("Ask AI About the Document:")
    user_query = st.text_input("Enter your question:")

    if st.button("Get Answer"):
        if user_query.strip():
            ai_response = query_gemini_ai(user_query, extracted_content)
            st.success("✅ AI Response:")
            st.write(ai_response)
        else:
            st.warning("⚠️ Please enter a question.")
