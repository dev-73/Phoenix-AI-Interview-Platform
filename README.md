
# 🔥 Phoenix AI Interview Platform

> **An AI-powered technical interview platform that automates candidate assessment using Google Gemini, live coding, voice interaction, intelligent evaluation, and recruiter analytics.**

---

## 📌 Overview

Phoenix is an enterprise-grade AI Interview Platform designed to automate technical interviews while maintaining a natural and engaging candidate experience.

Unlike traditional interview platforms that rely on static question banks, Phoenix dynamically adapts the interview based on:

- 📄 Candidate Resume
- 💼 Job Description
- 🎯 Experience Level
- 💬 Previous Responses
- 💻 Coding Performance

The platform generates a detailed Candidate Intelligence Report along with an explainable hiring recommendation to help recruiters make faster and more consistent hiring decisions.

---

## ✨ Key Features

### 🤖 AI Interview Engine
- Resume-aware technical interviews
- Adaptive questioning
- Human-like conversation
- Context-aware follow-up questions
- Dynamic interview flow

---

### 💻 Live Coding Assessment

Supports real-time coding interviews in multiple languages:

- Python
- SQL
- Java
- JavaScript
- C++
- Go
- Rust

Code execution is securely performed using the Piston API.

---

### 🎤 Voice Interview

- Speech-to-Text
- AI Voice Responses
- Natural conversation
- Interactive candidate experience

---

### 👁 Candidate Monitoring

Built-in proctoring features:

- Tab switching detection
- Copy/Paste monitoring
- Candidate activity tracking
- Interview integrity monitoring

---

### 📄 Resume Intelligence

Phoenix analyzes:

- Resume
- Job Description
- Skills
- Experience
- Resume-JD Match

The interview is automatically personalized for every candidate.

---

### 📊 AI Candidate Evaluation

The platform evaluates:

- Technical Knowledge
- Coding Ability
- Communication Skills
- Resume Match
- Candidate Behaviour

Final recommendation:

- ✅ Strong Hire
- 🟢 Hire
- 🟡 Follow-up
- ❌ Reject

---

# 🏗 System Architecture

```
Candidate
     │
     ▼
Streamlit Web Application
     │
     ▼
Interview Engine
     │
 ┌──────────────┐
 │ Google Gemini│
 │ Voice Engine │
 │ Coding Engine│
 └──────────────┘
     │
     ▼
Evaluation Engine
     │
     ▼
Candidate Intelligence Report
     │
     ▼
Hiring Recommendation
```

---

# 🛠 Tech Stack

| Category | Technologies |
|-----------|-------------|
| Language | Python |
| LLM | Google Gemini 2.5 Flash |
| Framework | Streamlit |
| Speech | Edge-TTS |
| Speech Recognition | SpeechRecognition |
| Database | SQLite |
| Visualization | Plotly |
| PDF Processing | PyPDF2 |
| Code Execution | Piston API |
| Deployment | Ngrok |

---

# 🚀 Workflow

```
Recruiter Configuration

        │
        ▼

Upload Resume

        │
        ▼

Upload Job Description

        │
        ▼

AI Generates Interview

        │
        ▼

Candidate Interview

        │
        ▼

Coding Assessment

        │
        ▼

AI Evaluation

        │
        ▼

Candidate Intelligence Report

        │
        ▼

Hiring Recommendation
```

---

# 📂 Project Structure

```
Phoenix-AI-Interview-Platform/

├── app.py
├── modules/
├── prompts/
├── assets/
├── screenshots/
├── docs/
├── requirements.txt
├── README.md
└── LICENSE
```

---

# 🎯 Future Enhancements

- Multi-Agent Interview Panel
- Video Interview Analysis
- Emotion Detection
- ATS Integration
- Microsoft Teams Integration
- Zoom Integration
- Docker Deployment
- Kubernetes Support
- Cloud Deployment
- Enterprise Analytics Dashboard

---

# 📸 Screenshots

Coming Soon

---

# 🎥 Demo

Coming Soon

---

# 👨‍💻 Author

**Dev Patel**

Data Scientist | AI & LLM Engineer

LinkedIn:
(Add your LinkedIn profile here)

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
