# 👾 BuddyAI – AI Companion with Chat & Report Generation

BuddyAI is a **Streamlit-based AI companion** that lets users **chat naturally** or **generate detailed reports** using the same clean chat interface.  
It blends conversation and research into a single experience, inspired by modern AI assistants.

🚀 **Live App Preview:**  
👉 https://ai-buddy-vanshh.streamlit.app/

---

## ✨ Features

### 💬 Chat Mode
- Natural AI conversation powered by **Google Gemini**
- Chat-style UI with message bubbles
- Session-based chat memory
- Clear chat functionality

### 📄 Report Generator Mode
- Generate **well-structured reports** from a single topic
- Automatically extracts **5 key points**
- Output appears directly in the chat UI
- Ideal for research, learning, and quick explanations

### 🔁 Smart Mode Switching
- Sidebar mode selector: **Chat / Report Generator**
- ⚠️ Switching modes **clears current chat or report state**
- Prevents mixing conversation history with report content

### 🎨 Modern Dark UI
- Custom dark theme using CSS
- Clean layout with focused chat bubbles
- Minimal and distraction-free design

---

## 🧠 Tech Stack

- **Frontend / UI**: Streamlit  
- **AI Models**:
  - Google Gemini (`gemini-2.5-flash`) – Chat & report generation
  - Hugging Face `google/flan-t5-base` – Key point summarization
- **Frameworks & Libraries**:
  - LangChain
  - Transformers (Hugging Face)
  - Python dotenv

---

## 📂 Project Structure

```
buddyai/
│
├── app.py          # Main Streamlit application
├── pipeline.py     # Report & key-point generation logic
├── README.md
├── requirements.txt
└── .env            # Environment variables (not committed)
```

---

## ▶️ Run Locally

### 1️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 2️⃣ Set environment variables
Create a `.env` file:
```env
GOOGLE_API_KEY=your_google_gemini_api_key
```

### 3️⃣ Run the app
```bash
streamlit run app.py
```

---

## ⚠️ Important Notes

- Switching modes **clears the current session state**
- First run may be slow due to Hugging Face model download
- Runs on CPU (no GPU required)
- Report outputs are treated as **tools**, not chat memory

---

## 🧭 Future Enhancements

- Slash commands (`/report topic`)
- Text summarization mode
- File upload & analysis
- Export reports as PDF
- Persistent chat memory
- Web search with citations

---

## 📜 License

This project is intended for **learning, experimentation, and personal use**.

---

## 🔹 Short Description

**BuddyAI** is a Streamlit-powered AI companion that allows users to chat naturally or generate detailed reports within the same chat interface.
