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

## 🔑 Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
GITHUB_TOKEN=your_github_token
```

## 1️⃣ Backend (FastAPI)


1. **Navigate to the backend directory:**
   ```bash
   cd backend 

2. **Install dependencies:**

```Bash
pip install -r requirements.txt
```


Start the FastAPI server:

```Bash
uvicorn main:app --reload 
```
Local API URL: http://127.0.0.1:8000

Interactive API Docs (Swagger): http://127.0.0.1:8000/docs

## 2️⃣ Frontend (Vanilla JavaScript)

Open a new terminal and navigate to the frontend directory:

```Bash
cd frontend
```

Start a local server:

```Bash
python -m http.server 5500
```

Access the application: Open http://localhost:5500 in your web browser.

## 3️⃣ Using the Application

- Open the frontend in your browser using the local server link above.
- Paste a Public GitHub Pull Request URL into the input field.

- Example: https://github.com/octocat/Hello-World/pull/1

Click **"Review Pull Request".**

## 📊 Review Results

Once the analysis is complete, the application will display:

**📝 AI-Generated Review Summary**

A clear breakdown of:
  - What files changed
  - Key code modifications
  - Overall intent of the PR

-----

**⚠️ Risk Score**

- An assessment of the PR’s:
  - Complexity
  - Potential impact
  - Risk level (low → high)

-----

**✅ Merge Recommendation**

- A data-driven suggestion on whether the PR should be:
 - Merged ✅
 - Reviewed further 🔍
 - Rejected ❌
