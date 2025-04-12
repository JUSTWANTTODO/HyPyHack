# Health Insurance Explainer Agent

An AI-powered assistant that helps users understand health insurance documents effortlessly.

This web-based application allows users to upload health insurance policy documents (PDF, DOCX, or TXT), extract key details, ask questions about them, and receive both textual and spoken explanations—all through a simple, user-friendly interface.

---

## Features

### 1. Intelligent Document Analysis
- Extracts and summarizes key details from health insurance policies.
- Supports multi-page PDFs, DOCX, and TXT formats.
- Identifies clauses, benefits, exclusions, and claim processes.

### 2. Multi-Lingual Support
- Explains policies in English and **Tenglish** (Telugu in English script).
- Improves accessibility for regional users.

### 3. OCR Integration
- Supports scanned documents via Optical Character Recognition.
- Extracts text from images or non-selectable PDFs.

### 4. Policy Comparison
- Compare two health policies and highlight key differences.
- Useful for decision-making between plans.

### 5. Voice Interaction
- Speech-to-text for voice-based questions.
- AI-generated spoken responses (text-to-speech).

### 6. Simplified Tenglish Summarization
- Generates easy-to-understand policy summaries in Tenglish.
- Breaks down complex insurance jargon.

---

## Tech Stack

| Technology       | Purpose                                 |
|------------------|------------------------------------------|
| Google Gemini AI | Document understanding & Q&A generation |
| Streamlit        | Frontend interface                      |
| PyPDF2           | PDF parsing                             |
| python-docx      | DOCX parsing                            |
| Tesseract OCR    | Text extraction from images             |
| SpeechRecognition| Converts speech to text                 |
| pyttsx3          | Text-to-speech for AI responses         |

---

## How It Works

1. Upload your health insurance document (PDF, DOCX, TXT, or scanned image).
2. Ask a question via text or voice input.
3. The AI processes the document and provides an easy-to-understand answer.
4. Optionally, receive a spoken response.
5. Compare two policy documents to identify differences.

---

## Challenges Faced

- **Multi-Lingual Support**: Tailoring responses for Tenglish.
- **OCR Accuracy**: Handling scanned or distorted text.
- **Contextual Understanding**: Interpreting insurance-specific terms.
- **Voice Input Handling**: Managing accent variation and background noise.

---

## Future Enhancements

- Support for additional languages (Kannada, Hindi, Tamil, etc.)
- Chat history and downloadable Q&A logs.
- Advanced comparison scoring between policies.
- Dedicated mobile application for wider reach.

---

## Installation & Setup

```bash
# Clone the repository
git clone https://github.com/JUSTWANTTODO/HyPyHack.git
cd HyPyHack

# Run the Streamlit app
streamlit run healthinsurancebot.py
```
