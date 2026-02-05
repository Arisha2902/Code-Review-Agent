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
