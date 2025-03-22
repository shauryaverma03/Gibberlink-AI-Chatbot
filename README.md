# 🚀 Gibberlink AI Chatbot

Gibberlink AI is a fun chatbot that can generate **gibberish responses** and normal responses using **OpenAI API**, **DeepSeek AI**, and **Gemini AI**.

---

## 📂 Project Structure

```
📂 Gibberlink-AI
 ┣ 📜 gibberlink_openai.py      # OpenAI API version
 ┣ 📜 gibberlink_deepseek.py    # DeepSeek AI version
 ┣ 📜 gibberlink_gemini.py      # Gemini AI version
 ┣ 📜 requirements_openai.txt   # Dependencies for OpenAI
 ┣ 📜 requirements_deepseek.txt # Dependencies for DeepSeek
 ┣ 📜 requirements_gemini.txt   # Dependencies for Gemini
 ┣ 📜 README.md                 # Documentation
 ┣ 📜 .gitignore                # Ignore unnecessary files
```

---

## 🔧 Installation

### Step 1️⃣: Clone the Repository
```sh
git clone https://github.com/shauryaverma03/Gibberlink-AI-Chatbot.git
cd Gibberlink-AI
```

### Step 2️⃣: Create a Virtual Environment
```sh
python -m venv gibberlink_env
```
- **Windows**: `gibberlink_env\Scripts\activate`
- **Mac/Linux**: `source gibberlink_env/bin/activate`

---

## 🛠️ Setup & Run

### **📌 1. OpenAI Version**
#### Install dependencies:
```sh
pip install -r requirements_openai.txt
```

#### Add OpenAI API Key:
Edit `gibberlink_openai.py` and replace:
```python
openai.api_key = "YOUR_OPENAI_API_KEY"
```

#### Run the chatbot:
```sh
python gibberlink_openai.py
```

---

### **📌 2. DeepSeek AI Version**
#### Install dependencies:
```sh
pip install -r requirements_deepseek.txt
```

#### Run the chatbot:
```sh
python gibberlink_deepseek.py
```

---

### **📌 3. Gemini AI Version**
#### Install dependencies:
```sh
pip install -r requirements_gemini.txt
```

#### Add Gemini API Key:
Edit `gibberlink_gemini.py` and replace:
```python
import google.generativeai as genai
genai.configure(api_key="YOUR_GEMINI_API_KEY")
```

#### Run the chatbot:
```sh
python gibberlink_gemini.py
```

---

## 📝 Features
✅ Generates **gibberish** and **normal** responses  
✅ Supports **OpenAI API** and **DeepSeek AI**  
✅ Includes **text-to-speech (TTS)** functionality  
✅ Easy setup with separate requirements files  

---

## 🤝 Contributing
Want to improve Gibberlink AI? Feel free to fork the repository and submit a pull request.  

---

## 📜 License
This project is licensed under the **MIT License**.

## ☕ Support Me  

If you enjoy my work, consider buying me a coffee! Your support keeps me going.  

<p align="center">
  <a href="https://www.buymeacoffee.com/shauryaverh" target="_blank">
    <img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me a Coffee" width="200">
  </a>
</p>
