# 🤖 Code Review Agent (ScaleDown Architecture)

An AI-powered system that automatically reviews **GitHub Pull Requests** using a **ScaleDown-inspired multi-agent architecture**.  
The system analyzes only PR diffs, detects issues, and generates concise review summaries to help developers review code faster and more effectively.

---

## 🚀 Features

- 🔗 GitHub Pull Request integration
- 🧠 AI-powered automated code review  
- 🧩 Multi-agent architecture:
  - Static Analysis Agent
  - Security Review Agent
  - Style & Maintainability Agent
  - Review Summarization Agent
- 📉 ScaleDown principles:
  - Diff-only analysis (no full repository scan)
  - Context compression
  - Agent-specific reasoning
- 🌐 Vanilla JavaScript frontend  
- ⚡ FastAPI backend  
- ☁️ Groq LLM used as the execution engine  

---

## 🏗️ Architecture Overview

Frontend (Vanilla JS)
|
v
FastAPI Backend
|
v
GitHub REST API ---> PR Diffs Only
|
v
Multi-Agent AI Pipeline
|
v
Groq LLM (Execution Layer)
|
v
Compressed Review Summary

## 🛠️ Tech Stack

### Backend
- Python
- FastAPI
- Groq LLM (`llama-3.1-8b-instant`)
- GitHub REST API

### Frontend
- HTML
- CSS
- Vanilla JavaScript

---


---

## 🔑 Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
GITHUB_TOKEN=your_github_token
```

1️⃣ Backend (FastAPI)
The backend manages the connection to GitHub and processes the AI analysis.

1. **Navigate to the backend directory:**
   ```bash
   cd backend
Install dependencies:

Bash
pip install -r requirements.txt
Start the FastAPI server:

Bash
uvicorn main:app --reload
Local API URL: http://127.0.0.1:8000

Interactive API Docs (Swagger): http://127.0.0.1:8000/docs

2️⃣ Frontend (Vanilla JavaScript)
The frontend is a lightweight interface for submitting PRs and viewing results.

Open a new terminal and navigate to the frontend directory:

Bash
cd frontend
Start a local server:

Bash
python -m http.server 5500
Access the application: Open http://localhost:5500 in your web browser.

3️⃣ Using the Application
Open the frontend in your browser using the local server link above.

Paste a Public GitHub Pull Request URL into the input field.

Example: https://github.com/octocat/Hello-World/pull/1

Click "Review Pull Request".

Review results: The application will display:

AI-generated review summary: A breakdown of what changed.

Risk score: An assessment of the PR's complexity or danger.

Merge recommendation: A data-driven suggestion on whether to merge.