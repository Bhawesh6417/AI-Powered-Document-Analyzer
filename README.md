# AI-Powered-Document-Analyzer
This code accepts different kinds of document and then accordingly analysed the data present and can answer different questions asked.
Overview

This project is a Streamlit-based AI-powered document analyzer that allows users to upload documents in various formats (PDF, CSV, Excel, and TXT) and extract textual content. Users can also ask AI-based queries about the extracted text using Google's Gemini AI model.

Features

Upload and process documents in PDF, CSV, Excel, and TXT formats.

Extract text from PDFs using pdfplumber.

Read and process CSV and Excel files using pandas.

Query extracted text using Google's Gemini AI.

User-friendly interface with Streamlit.

Requirements

Make sure you have the following installed:

Python 3.9+

Required Python libraries:

streamlit

pdfplumber

pandas

google-generativeai

Installation

Clone this repository:

git clone https://github.com/your-repo/ai-document-analyzer.git
cd ai-document-analyzer

Install dependencies:

pip install -r requirements.txt

Set up your API key for Gemini AI:

Replace GEMINI_API_KEY in app.py with your own Google Gemini API key.

Usage

Run the Streamlit application:

streamlit run app.py

Steps to Use:

Upload a document (PDF, CSV, Excel, or TXT).

View the extracted text.

Enter a query to analyze the document using Gemini AI.

Click Get Answer to receive AI-generated insights.

Code Breakdown

extract_text_from_pdf(pdf_file): Extracts text from a PDF using pdfplumber.

extract_data(file, file_type): Reads data from PDF, CSV, Excel, or TXT files.

query_gemini_ai(query, document_content): Sends user queries to Google's Gemini AI for analysis.

Streamlit UI: Provides an interactive interface for file upload, text display, and AI interaction.

Output

![image](https://github.com/user-attachments/assets/ccb29afb-cc98-41b8-b7f5-30751d54b3cc)

Excel File: 

![image](https://github.com/user-attachments/assets/c45392d4-7424-48a6-936e-bc6f1a886e1d)

Contributing

If you’d like to contribute, feel free to submit a pull request!

License

This project is licensed under the MIT License.
