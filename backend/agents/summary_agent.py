from scaledown_client import scaledown_analyze

def summarize_review(review_text):
    """
    Final Decision Agent:
    - Assign risk score (0–100)
    - Give merge recommendation
    - Explain decision
    """

    prompt = f"""
You are a senior code review decision agent.

Based on the following multi-agent code review:

1️⃣ Assign a Risk Score from 0 to 100
- 0–30  → Safe to Merge
- 31–70 → Review Carefully
- 71–100 → Do Not Merge

2️⃣ Give a Final Merge Recommendation
(MUST be exactly one of these):
- Safe to Merge
- Review Carefully
- Do Not Merge

3️⃣ Explain the decision in 2–3 bullet points

4️⃣ Then provide a short summarized review.

⚠️ VERY IMPORTANT OUTPUT FORMAT (follow strictly):

Risk Score: <number>

Final Merge Recommendation: <decision>

Reasoning:
- bullet point
- bullet point
- bullet point

Summary:
<short summary>

FULL REVIEW:
{review_text}
"""

    return scaledown_analyze(prompt)
