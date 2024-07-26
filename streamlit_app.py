import streamlit as st

# Display logo and title
st.image("Ani.ML_C_hrzHealth.png", width=200)  # Adjust the width as needed
st.title("ANI.ML Health PDF Reader")
st.subheader("Drag and Drop PDF to OCR")

import streamlit as st
import PyPDF2
import pytesseract
from pdf2image import convert_from_path
import tempfile

# Function to extract text from a PDF file
def pdf_to_text(file_path):
    # Create a PDF file reader object
    pdf_reader = PyPDF2.PdfReader(open(file_path, 'rb'))
    
    # Initialize an empty string to store the text
    text = ""
    
    # Loop through all the pages and extract text
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text += page.extract_text()
    
    return text

# Function to convert PDF to images and perform OCR
def pdf_to_ocr(file_path):
    # Convert PDF to a list of images
    images = convert_from_path(file_path)
    
    # Initialize an empty string to store the OCR text
    ocr_text = ""
    
    # Loop through all the images and perform OCR
    for image in images:
        ocr_text += pytesseract.image_to_string(image)
    
    return ocr_text

st.title("ANI.ML Health PDF Reader")

# File upload
uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file is not None:
    # Save the uploaded file to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
        temp_file.write(uploaded_file.getbuffer())
        temp_file_path = temp_file.name

    st.write("File uploaded successfully!")

    # Extract text from PDF
    if st.button("Extract Text"):
        text = pdf_to_text(temp_file_path)
        st.write("Text extracted from PDF:")
        st.text_area("PDF Text", text, height=200)

    # Perform OCR on PDF
    if st.button("Perform OCR"):
        ocr_text = pdf_to_ocr(temp_file_path)
        st.write("OCR text from PDF:")
        st.text_area("OCR Text", ocr_text, height=200)
