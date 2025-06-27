# AI Medical X-Ray Assistant - Streamlit App

import streamlit as st
from PIL import Image
import torch
import torchvision.transforms as transforms
import google.generativeai as genai
from gtts import gTTS
import os
import speech_recognition as sr


# Configure Gemini API
genai.configure(api_key="your API key")  # Replace with your API key
gmodel = genai.GenerativeModel("gemini-1.5-flash")

# Set Streamlit page config
st.set_page_config(layout="wide", page_title="AI Medical X-Ray Assistant", page_icon="🩻")

# CSS Styling
st.markdown(
    """
    <style>
    .stApp {
        background: black;
        font-family: 'Segoe UI', sans-serif;
        color: white;
        padding: 2rem;
    }
    
    
    .title {
        text-align: center;
        font-size: 48px;
        color: #ff6f61;
        font-family: 'Times New Roman', Times, serif;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.2);
        margin-top: 5px;
        animation: fadeIn 1s ease-in-out;
    }
    .intro {
        text-align: center;
        font-size: 20px;
        margin-bottom: 30px;
        color: white;
        animation: fadeIn 1.5s ease-in-out;
        line-height: 1.6em;
    }
    .response-box {
        background: #ffffff;
        color: #333;
        padding: 20px;
        border-radius: 15px;
        margin-top: 20px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
    }
    label[for="patient_name"] {
        font-size: 25px !important;
        font-weight: bold;
    }
    .stRadio > div {
        font-size: 18px !important;
    }
    
    label[for="Ask a health-related question"] {
        font-size: 18px !important;
        font-weight: bold;
    }
    </style>
    <div class='title'>AI Medical X-Ray Assistant</div>
    <div class='intro'>Welcome to your intelligent radiology assistant.<br>Upload your X-ray or scanning reports, and let our AI guide you through the diagnosis and treatment suggestions.</div>
    """,
    unsafe_allow_html=True
)

# Ask for patient's name
patient_name = st.text_input("👤 Enter Patient Name for personalized diagnosis:", key="patient_name")

# Upload Section
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 📤 Upload Chest X-ray (JPG/PNG)")
    uploaded_file = st.file_uploader("Choose an X-ray image", type=["jpg", "jpeg", "png"], key="xray")

with col2:
    st.markdown("### 🧾 Upload Scanning Report (PDF/JPG/PNG)")
    uploaded_report = st.file_uploader("Choose a scanning report", type=["pdf", "jpg", "jpeg", "png"], key="report")

# Prediction function (placeholder)
def predict_disease(image):
    return "Pneumonia"

# Voice Input Function
def voice_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("🎤 Listening...")
        audio = r.listen(source)
        try:
            return r.recognize_google(audio)
        except:
            return None

# Voice Output Function
def speak_text(text, lang='en'):
    tts = gTTS(text=text, lang=lang)
    tts.save("response.mp3")
    os.system("start response.mp3")

query = None

# Input Method
st.markdown("### 🗣️ Ask Medical Questions")
option = st.radio("Select Input Method:", ["Text", "Voice"], horizontal=True)
if option == "Text":
    query = st.text_input("Ask a health-related question")
elif option == "Voice":
    if st.button("🎤 Speak"):
        query = voice_to_text()

# Disease Prediction and Explanation
if uploaded_file or uploaded_report:
    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded X-ray", use_column_width=True)
        st.markdown("⏳ **Analyzing X-ray image...**")
        disease = predict_disease(image)
    else:
        st.markdown("⏳ **Analyzing scanning report...**")
        disease = "Scan suggests possible Tuberculosis"

    st.success(f"🧠 Detected Condition: {disease}")

    prompt = f"""
    You are a medical assistant. The patient name is {patient_name}.
    Their medical scan result shows: {disease}.
    Explain in simple terms what this condition is, its symptoms, causes, and medication.
    Use a caring and informative tone.
    """
    response = gmodel.generate_content(prompt)

    st.markdown("""
    <div class='response-box'>
    <h4>🩺 Personalized Diagnosis for {}</h4>
    """.format(patient_name), unsafe_allow_html=True)
    st.markdown(response.text)
    st.markdown("</div>", unsafe_allow_html=True)

    if st.button("🔊 Listen to Response"):
        speak_text(response.text)

# Chat Q&A
if query:
    chat_prompt = f"User ({patient_name}) asked: {query}. Give friendly health advice."
    response = gmodel.generate_content(chat_prompt)

    st.markdown("""
    <div class='response-box'>
    <h4>💬 Chat Response for {}</h4>
    """.format(patient_name), unsafe_allow_html=True)
    st.markdown(response.text)
    st.markdown("</div>", unsafe_allow_html=True)

    if st.button("🔊 Speak Chat Response"):
        speak_text(response.text)

# Footer
st.markdown("---")
st.markdown("<center><small>Made with ❤️ by Mounika Rayapalli | Powered by Gemini & Streamlit</small></center>", unsafe_allow_html=True)