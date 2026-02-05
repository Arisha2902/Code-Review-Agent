from scaledown_client import scaledown_analyze

def style_review(code):
    """
    Code Style Agent:
    - Readability
    - Naming
    - Formatting
    """

    prompt = f"""
You are a code style and maintainability reviewer.

Review the following code diff for:
- Poor naming conventions
- Readability issues
- Formatting problems
- Maintainability concerns

Provide improvement suggestions.

CODE DIFF:
{code}
"""

    return scaledown_analyze(prompt)
