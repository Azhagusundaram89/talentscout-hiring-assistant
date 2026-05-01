#  TalentScout Hiring Assistant

##  Project Overview

The TalentScout Hiring Assistant is an AI-powered chatbot designed to streamline the initial candidate screening process. It interacts with users through a chat-based interface, collects essential candidate details, and generates relevant technical interview questions based on the candidate’s declared tech stack.

The system ensures a structured and user-friendly experience by guiding candidates step-by-step through the data collection process while maintaining conversational flow.

---

##  Features

* Collects candidate details:

  * Full Name
  * Email Address
  * Phone Number
  * Experience
  * Desired Role
  * Location
  * Tech Stack
* Generates **3–5 technical questions per technology**
* Chat-based UI using Streamlit
* Stores candidate data in MySQL database
* Controlled conversation flow (no skipping fields)
* Clean and professional interaction

---

##  Installation Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Azhagusundaram89/talentscout-hiring-assistant.git
cd talentscout-hiring-assistant
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Setup Environment Variable

```bash
setx GROQ_API_KEY "your_api_key_here"
```

Restart terminal after setting this.

---

### 4. Setup MySQL Database

Open MySQL and run:

```sql
CREATE DATABASE talentscout;

USE talentscout;

CREATE TABLE candidates (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(20),
    experience VARCHAR(20),
    role VARCHAR(100),
    location VARCHAR(100),
    tech_stack TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

### 5. Update Database Credentials

In `db.py`, update:

```python
user="root"
password="YOUR_PASSWORD"
```

---

### 6. Run the Application

```bash
streamlit run app.py
```

Open browser:

```
http://localhost:8501
```

---

##  Usage Guide

1. Launch the application
2. The chatbot will greet you and start asking questions
3. Enter your details step-by-step
4. After providing your tech stack:

   * The system generates technical questions
5. The conversation ends with a confirmation message
6. Data is stored in the MySQL database

---

## 🛠 Technical Details

### Technologies Used

* Python
* Streamlit (Frontend UI)
* Groq API (LLM inference)
* MySQL (Database)
* Requests (API communication)

### Model Details

* Model: LLaMA 3.1 (via Groq API)
* Fast inference and low latency
* Used specifically for generating technical questions

### Architecture

* **Frontend:** Streamlit chat interface
* **Backend:** Python logic with step-based control
* **Database:** MySQL for structured storage
* **LLM Integration:** Groq API for question generation

---

##  Prompt Design

Prompting was designed carefully to ensure:

### 1. Controlled Information Gathering

Instead of relying fully on the LLM, a **step-based flow** is implemented in code to:

* Ensure all required fields are collected
* Avoid skipping or random responses

### 2. Technical Question Generation

A structured prompt is used:

* Takes user tech stack as input
* Generates 3–5 questions per skill
* Ensures clarity and relevance

Example prompt:

> "Generate 3–5 technical interview questions for: Python, Django. Keep them clear and professional."

### 3. Context Handling

* Chat history is maintained using session state
* Ensures continuity in conversation

---

##  Challenges & Solutions

###  Challenge 1: LLM giving inconsistent responses

**Solution:**
Implemented a **step-by-step controlled flow** instead of relying fully on LLM.

---

###  Challenge 2: API key exposure issue

**Solution:**
Used environment variables (`GROQ_API_KEY`) and `.gitignore` to secure sensitive data.

---

###  Challenge 3: GitHub push blocked (secret detection)

**Solution:**
Removed git history and re-initialized repository without secrets.

---

###  Challenge 4: Maintaining conversation context

**Solution:**
Used `st.session_state` to store chat and control flow.

---

###  Challenge 5: Data storage scalability

**Solution:**
Replaced JSON storage with MySQL for structured and scalable data handling.

---

## Future Enhancements

* Candidate dashboard (view stored data)
* Email validation & input validation
* Export candidate data (CSV)
* Deploy on cloud (Streamlit Cloud / AWS)
* Multi-language support

---

## Conclusion

This project demonstrates the effective use of LLMs in real-world applications by combining structured logic with AI capabilities. It ensures reliability, scalability, and a smooth user experience for candidate screening.

---
