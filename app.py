import streamlit as st
import PyPDF2

st.title("📄 Resume Analyzer")

uploaded_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])

if uploaded_file:
    st.success("File uploaded successfully ✅")

    # read PDF
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    text = ""

    for page in pdf_reader.pages:
        text += page.extract_text()

    st.write("### Extracted Text")
    st.write(text)

    # simple analysis
    st.write("### Analysis Result")

    if "python" in text.lower():
        st.write("✅ Python skill detected")
    else:
        st.write("❌ Python skill not found")

    if "project" in text.lower():
        st.write("✅ Projects mentioned")
    else:
        st.write("❌ Add projects to your resume")

    st.write("⚡ Basic Score: 7/10")