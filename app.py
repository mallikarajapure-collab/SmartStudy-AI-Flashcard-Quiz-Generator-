import streamlit as st
import google.generativeai as genai
from pypdf import PdfReader

# Page setup
st.set_page_config(
    page_title="SmartStudy AI",
    page_icon="📚"
)

st.title("📚 SmartStudy AI")
st.subheader("AI Flashcard & Quiz Generator")

# Store generated result
if "result" not in st.session_state:
    st.session_state.result = ""

# API Key
api_key = st.text_input(
    "Enter your Gemini API Key",
    type="password"
)

if api_key:
    genai.configure(api_key=api_key)

    model = genai.GenerativeModel("gemini-2.5-flash")

    uploaded_file = st.file_uploader(
        "Upload your notes PDF",
        type="pdf"
    )

    notes = ""

    # PDF reading
    if uploaded_file:
        pdf_reader = PdfReader(uploaded_file)

        for page in pdf_reader.pages:
            text = page.extract_text()

            if text:
                notes += text

        if notes:
            st.success("PDF uploaded successfully!")

    # Manual notes
    text_notes = st.text_area(
        "Or paste your notes here",
        height=200
    )

    if text_notes:
        notes = text_notes

    # Generate button
    if st.button("Generate Flashcards & Quiz"):

        if notes.strip() == "":
            st.warning("Please upload PDF or enter notes.")

        else:
            prompt = f"""
You are an AI Study Assistant.

Generate:

1. Five Flashcards with Question and Answer.

2. Five Multiple Choice Questions with correct answers.

Make the output clean and easy to study.

Notes:
{notes}
"""

            with st.spinner("Generating content..."):
                response = model.generate_content(prompt)

            st.session_state.result = response.text

            st.success("Generated Successfully!")

    # Show result
if st.session_state.result:

    st.success("Generated Successfully!")

    tab1, tab2 = st.tabs(["📚 Flashcards", "📝 Quiz"])

    with tab1:
        st.markdown("## 📚 Your Flashcards")
        st.markdown(st.session_state.result)

    with tab2:
        st.markdown("## 📝 Your Quiz")
        st.markdown(st.session_state.result)

    st.download_button(
        label="📥 Download Flashcards & Quiz",
        data=st.session_state.result,
        file_name="SmartStudy_AI_Flashcards.txt",
        mime="text/plain"
    )