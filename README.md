🏥 Health Insurance Explainer Agent
🚀 An AI-powered assistant that helps users understand health insurance documents effortlessly!

This tool allows users to upload health insurance policies in PDF, DOCX, or TXT format, extract key details, ask questions about them, and even receive spoken responses—all in a simple, intuitive interface.

📌 Features
🏷️ Intelligent Document Analysis
Extracts and summarizes key details from health insurance policy documents.
Supports multi-page PDFs, DOCX, and TXT files.
Identifies important clauses, benefits, exclusions, and claim processes.
🌍 Multi-Lingual Support
Provides policy explanations in English and Tenglish (Telugu written in English letters).
Enhances accessibility for regional users.
🔍 OCR Integration
Supports scanned documents through Optical Character Recognition (OCR).
Extracts text from images or non-selectable PDFs.
📄 Policy Comparison
Compare two health insurance policies and highlight key differences.
Useful for users deciding between multiple insurance plans.
🎙️ Voice Interaction
Speech-to-Text: Users can ask questions via voice input.
AI Voice Response: AI-generated text-to-speech explanations for better accessibility.
📝 Summarization in Tenglish
Generates simple, easy-to-understand summaries of policies in Tenglish.
Helps users grasp complex insurance terms quickly.
🏗️ Tech Stack
Technology	Purpose
🤖 Google Gemini AI	Intelligent document analysis & response generation
🖥️ Streamlit	Interactive and user-friendly interface
📄 PyPDF2, python-docx	Document parsing & text extraction
🔍 OCR (Tesseract or Google OCR)	Extracts text from scanned images/PDFs
🎤 Speech Recognition	Converts voice queries into text
🔊 pyttsx3	AI-generated text-to-speech responses
🚀 How It Works
1️⃣ Upload your health insurance document (PDF, DOCX, TXT, or Scanned Image).
2️⃣ Ask any question about the policy through text or voice input.
3️⃣ The AI analyzes the document and provides concise, easy-to-understand answers.
4️⃣ Optionally, get a spoken response for better accessibility.
5️⃣ Compare different policies to identify key differences and important clauses.

⚡ Challenges Faced
✅ Multi-Lingual Support: Implementing Tenglish required fine-tuning AI responses.
✅ OCR Accuracy: Extracting text from scanned PDFs/images while handling distorted text.
✅ Context Awareness: Ensuring AI understands insurance-specific terms and conditions.
✅ Speech Recognition: Handling different accents and background noise for voice input.

💡 Future Enhancements
🚀 More Language Support (Kannada, Hindi, Tamil, etc.)
🚀 Chat History Storage for revisiting past interactions
🚀 Advanced Comparison Metrics for insurance policies
🚀 Mobile App Version for better accessibility

🛠️ Installation & Setup
Clone the Repository

bash
Copy
Edit
git clone https://github.com/your-repo-name.git
cd your-repo-name
Install Dependencies

bash
Copy
Edit
pip install -r requirements.txt
Run the Application

bash
Copy
Edit
streamlit run app.py
