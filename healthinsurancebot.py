import os
import streamlit as st
import pyttsx3
import speech_recognition as sr
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain_google_genai import ChatGoogleGenerativeAI, HarmBlockThreshold, HarmCategory
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from docx import Document  # For DOCX support

# Load environment variables
load_dotenv()

# Initialize the LLM model
llm = ChatGoogleGenerativeAI(
    temperature=0.7,
    model="gemini-1.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    safety_settings={HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE}
)

# Extract text from PDF
def extract_pdf_text(pdf_file):
    reader = PdfReader(pdf_file)
    return "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])

# Extract text from DOCX
def extract_docx_text(docx_file):
    doc = Document(docx_file)
    return "\n".join([para.text for para in doc.paragraphs])

# Extract text from TXT
def extract_txt_text(txt_file):
    return txt_file.read().decode("utf-8")

# Extract text based on file type
def extract_text(file):
    file_type = file.name.split(".")[-1].lower()
    if file_type == "pdf":
        return extract_pdf_text(file)
    elif file_type == "docx":
        return extract_docx_text(file)
    elif file_type == "txt":
        return extract_txt_text(file)
    else:
        return None

# Define prompt templates
prompt_template = PromptTemplate(
    input_variables=["data", "query"],
    template="""You are a helpful chatbot that explains health insurance details in a simple and friendly manner.
    Given the extracted document, answer the user's question based on its contents.

    Document Content:
    {data}

    User Query:
    {query}

    Provide a clear and concise answer.
    """
)

summary_prompt_template = PromptTemplate(
    input_variables=["data"],
    template="""Summarize the following document in Tenglish (Telugu words written in English letters):

    Document Content:
    {data}

    Provide a short and simple summary in Tenglish.
    """
)

# Set up LangChain processing
llm_chain = prompt_template | llm | StrOutputParser()
summary_chain = summary_prompt_template | llm | StrOutputParser()

# Function to recognize speech
def recognize_speech():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        st.write("Listening... (You can speak)")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        try:
            audio = recognizer.listen(source)
            text = recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            st.write("Sorry, I didn't catch that.")
            return ""
        except sr.RequestError as e:
            st.write(f"Speech recognition service error: {e}")
            return ""

# Function to speak response
def speak_response(response):
    engine = pyttsx3.init()
    try:
        clean_response = ''.join(char for char in response if char.isprintable())
        engine.say(clean_response)
        engine.runAndWait()
    except Exception as e:
        st.write(f"Error in TTS: {e}")
    finally:
        engine.stop()

# Streamlit UI
st.set_page_config(page_title="Health Insurance Chatbot", layout="centered")
st.title("Health Insurance Chatbot")
st.write("Upload your health insurance policy document and chat with the AI!")

# File uploader
uploaded_file = st.file_uploader("Upload a document (PDF, DOCX, TXT)", type=["pdf", "docx", "txt"])

if uploaded_file:
    try:
        extracted_text = extract_text(uploaded_file)
        
        if not extracted_text:
            st.error("Unsupported file format or empty document.")
        else:
            st.write(f"**Extracted Data from {uploaded_file.name}**")
            st.text_area("Extracted Content Preview", extracted_text[:1000], height=150, disabled=True)

            # Initialize chat session
            if "chat_history" not in st.session_state:
                st.session_state.chat_history = []
                st.session_state.pdf_text = extracted_text

            # Display chat history
            st.write("**Chat with AI:**")
            for message in st.session_state.chat_history:
                st.markdown(f"**{message['role']}:** {message['content']}")

            # User input field
            user_input = st.text_input("Ask a question about your document...")
            if st.button("Speak Instead"):
                user_input = recognize_speech()
                st.text_input("Recognized Speech:", user_input, disabled=True)

            if user_input:
                chat_response = llm_chain.invoke({"data": st.session_state.pdf_text, "query": user_input})

                # Store conversation
                st.session_state.chat_history.append({"role": "User", "content": user_input})
                st.session_state.chat_history.append({"role": "AI", "content": chat_response})

                # Display AI response
                st.write(f"**AI:** {chat_response}")
                speak_response(chat_response)

            # Generate Tenglish summary
            if st.button("Get Summary in Tenglish"):
                summary_response = summary_chain.invoke({"data": st.session_state.pdf_text})
                st.write("**Summary in Tenglish:**")
                st.markdown(summary_response)

    except Exception as e:
        st.error(f"Error processing file: {e}")

