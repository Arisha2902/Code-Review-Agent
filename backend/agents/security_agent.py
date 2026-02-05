from scaledown_client import scaledown_analyze

def security_review(code):
    """
    Security Review Agent:
    - Secrets
    - Injections
    - Unsafe APIs
    """

    prompt = f"""
You are a security review agent.

Analyze the following code diff and identify:
- Hardcoded secrets or credentials
- SQL / command injection risks
- Unsafe system or file operations
- Authentication or authorization flaws

Classify issues as:
- Critical
- Medium
- Low

CODE DIFF:
{code}
"""

    return scaledown_analyze(prompt)
