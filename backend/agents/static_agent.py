from scaledown_client import scaledown_analyze

def static_review(code):
    """
    Static Analysis Agent:
    - Bugs
    - Logic errors
    - Performance issues
    """

    prompt = f"""
You are a senior software engineer performing static code analysis.

Analyze the following GitHub Pull Request diff and identify:
- Bugs or logical errors
- Performance issues
- Bad coding practices

Respond in clear bullet points.

CODE DIFF:
{code}
"""

    return scaledown_analyze(prompt)
