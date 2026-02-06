from scaledown_client import scaledown_analyze

# def style_review(code):
#     """
#     Code Style Agent:
#     - Readability
#     - Naming
#     - Formatting
#     """

#     prompt = f"""
# You are a code style and maintainability reviewer.

# Review the following code diff for:
# - Poor naming conventions
# - Readability issues
# - Formatting problems
# - Maintainability concerns

# Provide improvement suggestions.

# CODE DIFF:
# {code}
# """

#     return scaledown_analyze(prompt)


def style_review(code):
    prompt = f"""
You are a senior engineer doing a harsh code review.

Rules:
- Enforce clean code principles
- Penalize inconsistent naming
- Penalize large functions
- Penalize inline logic
- Penalize missing comments

Look for:
- Naming problems
- Formatting inconsistencies
- Code duplication
- Overly complex logic
- Poor separation of concerns

Classify issues as Medium or Low.

CODE DIFF:
{code}

If code looks fine, suggest refactors anyway.
"""
    return scaledown_analyze(prompt)
