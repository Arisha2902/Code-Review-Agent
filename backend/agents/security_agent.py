from scaledown_client import scaledown_analyze

# def security_review(code):
#     """
#     Security Review Agent:
#     - Secrets
#     - Injections
#     - Unsafe APIs
#     """

#     prompt = f"""
# You are a security review agent.

# Analyze the following code diff and identify:
# - Hardcoded secrets or credentials
# - SQL / command injection risks
# - Unsafe system or file operations
# - Authentication or authorization flaws

# Classify issues as:
# - Critical
# - Medium
# - Low

# CODE DIFF:
# {code}
# """

#     return scaledown_analyze(prompt)


def security_review(code):
    prompt = f"""
You are a paranoid security engineer.

Assume attackers WILL exploit this code.

Rules:
- Treat client-side storage as insecure by default
- Treat missing authentication as a security flaw
- Treat missing validation as a vulnerability
- Flag ANY risky pattern, even if theoretical

Look for:
- Hardcoded secrets
- Insecure storage (localStorage, cookies, globals)
- Missing auth checks
- Injection risks
- Unsafe APIs or system calls

Severity rules:
- Critical: exploitable vulnerability
- Medium: weak security design
- Low: insecure practice

CODE DIFF:
{code}

Be strict. Over-report if unsure.
"""
    return scaledown_analyze(prompt)
