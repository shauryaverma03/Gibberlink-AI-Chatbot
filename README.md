# Gibberlink

# 🚀 Gibberlink AI Chatbot

Gibberlink AI is a fun chatbot that can generate **gibberish responses** and normal responses using either **OpenAI API** or **DeepSeek AI**.

---

## 📂 Project Structure

```
📂 Gibberlink-AI
 ┣ 📜 gibberlink_openai.py      # OpenAI API version
 ┣ 📜 gibberlink_deepseek.py    # DeepSeek AI version
 ┣ 📜 requirements_openai.txt   # Dependencies for OpenAI
 ┣ 📜 requirements_deepseek.txt # Dependencies for DeepSeek
 ┣ 📜 README.md                 # Documentation
 ┣ 📜 .gitignore                # Ignore unnecessary files
```

---

## 🔧 Installation

### Step 1️⃣: Clone the Repository
```sh
git clone https://github.com/your-username/Gibberlink-AI.git
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
