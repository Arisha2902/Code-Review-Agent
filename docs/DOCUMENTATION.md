
# 📘 Code Review Agent – Project Documentation (HPE GenAI)

## Project Overview

The Code Review Agent is a GenAI-powered system designed to assist developers during GitHub Pull Request reviews.
It analyzes only the Pull Request diffs and provides clear, actionable feedback along with a final merge recommendation.

The project focuses on **practical AI usage**, efficiency, and developer productivity rather than full repository analysis.

---

## How the System Works

1. A user submits a GitHub Pull Request URL.
2. The backend fetches only the changed code (PR diff).
3. Multiple AI agents independently analyze the code for:

   * Code quality
   * Security risks
   * Style and maintainability
4. A final decision agent aggregates the feedback and:

   * Assigns a **risk score (0–100)**
   * Provides a **merge recommendation**
5. Results are displayed in a simple, visual frontend.

---

## Creative / Unique Feature

The key innovation is a **risk-based merge decision layer** built on top of GenAI analysis.
Instead of only listing issues, the system converts AI feedback into a single risk score and a clear recommendation (*Safe to Merge*, *Review Carefully*, or *Do Not Merge*).

This makes AI output easier to understand and more useful in real-world development workflows.

---

## GenAI Value Proposition

* Uses GenAI for **decision support**, not just text generation
* Reduces review time by focusing on **diff-only analysis**
* Improves clarity by converting complex feedback into actionable insights
* Demonstrates responsible and efficient AI usage

---

## Technologies Used

* FastAPI (Backend)
* Groq LLM (AI execution engine)
* GitHub REST API
* Vanilla JavaScript, HTML, CSS (Frontend)

---

## Challenges & Learnings

Key challenges included handling API changes, resolving frontend-backend integration issues, and ensuring consistent AI output formatting.
Solving these helped improve system robustness and reinforced full-stack debugging skills.

---

## Conclusion

This project demonstrates how GenAI can be effectively applied to software engineering workflows.
By combining multi-agent analysis with a risk-based decision system, the Code Review Agent delivers meaningful, enterprise-ready insights for Pull Request reviews.

