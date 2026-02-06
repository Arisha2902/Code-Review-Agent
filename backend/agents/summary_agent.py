from scaledown_client import scaledown_analyze

# def summarize_review(review_text):
#     """
#     Final Decision Agent:
#     - Assign risk score (0–100)
#     - Give merge recommendation
#     - Explain decision
#     """

#     prompt = f"""
# You are a senior code review decision agent.

# Based on the following multi-agent code review:

# 1️⃣ Assign a Risk Score from 0 to 100
# - 0–30  → Safe to Merge
# - 31–70 → Review Carefully
# - 71–100 → Do Not Merge

# 2️⃣ Give a Final Merge Recommendation
# (MUST be exactly one of these):
# - Safe to Merge
# - Review Carefully
# - Do Not Merge

# 3️⃣ Explain the decision in 2–3 bullet points

# 4️⃣ Then provide a short summarized review.

# ⚠️ VERY IMPORTANT OUTPUT FORMAT (follow strictly):

# Risk Score: <number>

# Final Merge Recommendation: <decision>

# Reasoning:
# - bullet point
# - bullet point
# - bullet point

# Summary:
# <short summary>

# FULL REVIEW:
# {review_text}
# """

#     return scaledown_analyze(prompt)

# def final_decision_review(review_text):
#     prompt = f"""
# You are a senior tech lead making a merge decision.

# Steps:
# 1. Assign a RISK SCORE from 0–100
#    - 0–30: Safe
#    - 31–60: Review Carefully
#    - 61–100: Do Not Merge

# 2. Give a FINAL MERGE DECISION:
#    - Safe to Merge
#    - Review Carefully
#    - Do Not Merge

# 3. Explain decision in 2–3 bullets ONLY.

# Rules:
# - Be strict
# - Penalize security and design flaws heavily
# - Prefer safety over speed

# FULL REVIEW:
# {review_text}

# Return in this exact format:

# Risk Score: <number>
# Final Decision: <decision>
# Reason:
# - bullet
# - bullet
# """
#     return scaledown_analyze(prompt)

def summarize_review(review_text):
    prompt = f"""
You are a STRICT senior software reviewer.

Based on the analysis below:

1. Assign a Risk Score from 0 to 100
   - 0–30 = Safe
   - 31–70 = Review Carefully
   - 71–100 = Do Not Merge

2. Give ONE final merge decision:
   - Safe to Merge
   - Review Carefully
   - Do Not Merge

3. List issues aggressively.
   - If code is weak, SAY SO.
   - Do NOT be polite.
   - Assume production standards.

Format EXACTLY like this:

Risk Score: <number>
Decision: <decision>

### Critical Issues
- item (or "None")

### Medium Priority Issues
- item (or "None")

### Minor Suggestions
- item (or "None")

ANALYSIS:
{review_text}
"""
    return scaledown_analyze(prompt)
