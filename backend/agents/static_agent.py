from scaledown_client import scaledown_analyze

# def static_review(code):
#     """
#     Static Analysis Agent:
#     - Bugs
#     - Logic errors
#     - Performance issues
#     """

#     prompt = f"""
# You are a senior software engineer performing static code analysis.

# Analyze the following GitHub Pull Request diff and identify:
# - Bugs or logical errors
# - Performance issues
# - Bad coding practices

# Respond in clear bullet points.

# CODE DIFF:
# {code}
# """

#     return scaledown_analyze(prompt)

def static_review(code):
    prompt = f"""
You are a VERY STRICT static code review agent.

Your job is to FIND PROBLEMS aggressively.

Rules:
- Assume the code will run in production.
- If best practices are missing, mark them as issues.
- If something is unclear, treat it as a potential bug.
- Penalize bad naming, unclear logic, magic values, missing comments.

Identify:
- Logical errors
- Poor code structure
- Readability issues
- Missing validations
- Anti-patterns

Classify findings as:
- Critical (breaks functionality or logic)
- Medium (maintainability, bugs waiting to happen)
- Low (style, clarity)

CODE DIFF:
{code}

DO NOT say "No issues found".
If nothing obvious exists, suggest what SHOULD be improved.
"""
    return scaledown_analyze(prompt)
