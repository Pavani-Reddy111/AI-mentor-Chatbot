# 🤖 AI Mentor Chatbot

## 📌 Overview
AI Mentor Chatbot is a **module-based AI learning assistant** built using **Streamlit**, **LangChain**, and **Google Gemini**.  
The chatbot provides **focused, domain-restricted mentoring** by answering questions **only from the selected learning module**.

---

## 🎯 Key Features
- Module-based AI mentoring
- Strict domain restriction
- Beginner-friendly explanations
- Session-based chat memory
- Download chat history as `.txt`
- Clean Streamlit UI

---

## 📚 Available Modules
- Python
- SQL
- Power BI
- Exploratory Data Analysis (EDA)
- Machine Learning (ML)
- Deep Learning (DL)
- Generative AI (Gen AI)
- Agentic AI

---

## 🧠 How It Works
1. User selects a learning module
2. AI acts as a dedicated mentor for that module
3. Relevant questions are answered
4. Irrelevant questions are politely rejected
5. Chat history is stored and downloadable

---

## 🏗️ Tech Stack
- **Frontend:** Streamlit  
- **LLM:** Google Gemini  
- **AI Framework:** LangChain  
- **Language:** Python  

---

## 📁 Project Structure
```
ai-mentor-chatbot/
├── app.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup & Run Locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

Create a `.env` file:
```
GOOGLE_API_KEY=your_api_key_here
```

---

## ☁️ Deploy on Streamlit Cloud
1. Push code to GitHub
2. Create a Streamlit Cloud app
3. Set main file as `app.py`
4. Add secret:
```
GOOGLE_API_KEY = "your_api_key_here"
```

---

## 📥 Chat Download Feature
- Download complete conversation
- Useful for revision and interview prep

---

## 🎓 Learning Outcomes
- Domain-restricted chatbot design
- Prompt engineering for controlled AI responses
- Streamlit + LangChain integration
- Real-world AI mentor system implementation

---

## 👩‍💻 Author
**Pavani Reddy**
