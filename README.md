<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:312E81,50:7C3AED,100:F0ABFC&height=220&section=header&text=SMARTSTUDY%20AI&fontSize=42&fontColor=FFFFFF&fontAlignY=36&desc=Turn%20Your%20Notes%20Into%20Revision%20Material&descAlignY=60&descSize=14" width="100%" alt="Violet and lavender study header" />

<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
<img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit" />
<img src="https://img.shields.io/badge/Gemini-4285F4?style=for-the-badge&logo=google&logoColor=white" alt="Gemini" />

</div>

---

## 📚 Overview

**SmartStudy AI Flashcard & Quiz Generator** is a Streamlit study helper that uses the Gemini API to generate revision content from notes. Users can upload a PDF or paste notes, then request five flashcards and five multiple-choice questions.

## ✨ Features

- Accept study notes from a PDF or text box.
- Extract readable text from PDF pages with PyPDF.
- Generate flashcards and quiz questions using Gemini.
- Keep the generated response in the Streamlit session.
- Download the generated content as a text file.

## 🧰 Tech Stack

- Python
- Streamlit
- Google Generative AI Python SDK
- Gemini model: `gemini-2.5-flash`
- PyPDF

## 🚀 Setup

1. Clone or download the repository.
2. Create and activate a virtual environment.
3. Install dependencies from the repository's `requirement.txt` file:

```bash
pip install -r requirement.txt
```

4. Start the app:

```bash
python -m streamlit run app.py
```

5. Enter your Gemini API key in the app, upload a PDF or paste notes, and select **Generate Flashcards & Quiz**.

## 🔄 Workflow

1. Provide a Gemini API key.
2. Upload a PDF or paste study notes.
3. The app builds a prompt requesting five flashcards and five multiple-choice questions.
4. Review the generated response and download it as a text file.

## ⚠️ Notes & Limitations

- A Gemini API key and network access are needed for generation.
- PDF text extraction depends on the PDF containing extractable text; scanned pages may need OCR.
- The current interface displays the same generated response in both the Flashcards and Quiz tabs, so the sections are not independently parsed yet.
- AI-generated answers may contain errors; verify them against your course material.
- Avoid uploading private or sensitive documents.

## 🔮 Future Improvements

- Parse flashcards and quiz questions into separate structured sections.
- Add answer selection and quiz scoring.
- Save study sets and track progress.
- Add support for scanned PDFs with OCR.

---

<div align="center"><sub>Active recall • Study productivity • Generative AI</sub></div>