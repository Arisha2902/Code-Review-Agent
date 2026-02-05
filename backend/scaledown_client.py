from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def scaledown_analyze(prompt: str) -> str:
    """
    ScaleDown-style analysis using Groq as the execution engine.
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",

        messages=[
            {
                "role": "system",
                "content": (
                    "You are a ScaleDown-powered AI code review agent. "
                    "Be concise, structured, and focus on high-impact issues."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content
