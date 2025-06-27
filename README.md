# 🩺 AI Medical X-Ray Assistant

Welcome to the **AI Medical X-Ray Assistant** — an intelligent healthcare companion built with **Streamlit**, **Gemini AI**, and **Computer Vision**. This project is designed to assist patients and healthcare providers by analyzing medical X-rays or scanning reports and generating a human-friendly explanation of the diagnosis and recommended treatments.


---

##  Project Purpose

This project aims to:
- Provide an easy-to-use interface for patients to upload their **Chest X-ray** or **Scanning Reports**.
- Use AI to **detect potential diseases** from medical images.
- Generate **explanations and medication suggestions** in a caring, conversational tone using **Gemini 1.5 Flash**.
- Allow patients to **interact via voice or text** to ask health-related questions.
- Enable **text-to-speech** output for those who prefer listening over reading.

---

## 💡 Key Features

### 📷 Upload Medical Data
- Upload **X-ray images** in JPG/PNG format.
- Upload **scanning reports** in PDF or image format.

### 🤖 AI-Powered Diagnosis
- Predicts conditions (like pneumonia, TB) based on uploaded scans.
- Uses **Google Gemini AI** to explain the diagnosis, symptoms, causes, and medications.

### 🗣️ Voice & Text Interaction
- Patients can ask health-related queries using **voice** or **text input**.
- Real-time voice recognition via `SpeechRecognition`.
- Voice output generated using `gTTS`.

### 🎨 Beautiful UI
- Dark-themed responsive design using custom HTML/CSS inside Streamlit.
- Clear and intuitive layout for all types of users.

---

## 🛠️ Tech Stack

| Tech | Purpose |
|------|---------|
| **Python** | Core programming language |
| **Streamlit** | Frontend Web App Framework |
| **Gemini 1.5 Flash (Google Generative AI)** | Natural language medical explanations |
| **OpenCV & PIL** | Image handling and preprocessing |
| **SpeechRecognition** | Voice input from microphone |
| **gTTS (Google Text-to-Speech)** | Converts responses to voice |
| **Torch** | Placeholder for future ML model integration |

---

## 🚀 How to Run the App Locally

1. **Clone the Repository**

git clone https://github.com/yourusername/ai-medical-xray-assistant.git
cd ai-medical-xray-assistant
Create a Virtual Environment & Install Requirements

2.Create a Virtual Environment & Install Requirements:

python -m venv .venv
source .venv/bin/activate    # Linux/Mac
.venv\Scripts\activate       # Windows
pip install -r requirements.txt

pip install -r requirements.txt
Set Your Gemini API Key
Replace "your API key" in app.py with your Gemini API key.

Run the App

bash
Copy
Edit
streamlit run app.py
📁 Folder Structure
bash
Copy
Edit
├── app.py                  # Main Streamlit application
├── requirements.txt        # Required dependencies
├── assets/                 # Optional: images, icons
└── README.md               # Project documentation
🧪 Example Use Case
A user uploads a chest X-ray image.

The app predicts a condition like "Pneumonia".

Gemini AI explains what Pneumonia is, its symptoms, treatment, and advice.

The user asks follow-up questions like "Can I recover at home?" via voice or text.

AI responds with caring and informative guidance, optionally as audio.

🙋‍♀️ Made With Love By
👩‍💻 Mounika Rayapalli
Passionate about using AI for real-world health solutions and making technology more human-centric.

“I believe in using tech to simplify lives — especially when it comes to health.”

📌 Note
This project is a prototype and not a substitute for professional medical advice.

Always consult certified medical professionals for any diagnosis or treatment.

🌐 License
This project is licensed under the MIT License.

🔗 Connect
🔗 LinkedIn

🌐 Portfolio

📧 rayapallimounika@example.com

yaml
Copy
Edit

---

### ✅ Tips:
- Replace `"your API key"` in the code.
- Replace all placeholders like `yourusername`, `yourimageurl.com`, and contact links with actual values.
- You can also add a `requirements.txt` if you haven't already (`pip freeze > requirements.txt`).

Let me know if you want me to generate a banner or diagram to include!