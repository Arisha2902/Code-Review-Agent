from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware


from github import fetch_pr_files
from agents.static_agent import static_review
from agents.security_agent import security_review
from agents.style_agent import style_review
# from agents.summary_agent import final_decision_review
from agents.summary_agent import summarize_review


# Load environment variables (.env)
load_dotenv()

app = FastAPI(
    title="Code Review Agent",
    description="ScaleDown-powered AI agent for GitHub Pull Request reviews",
    version="1.0"
)

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],   # allow all origins (OK for dev & hackathon)
#     allow_credentials=True,
#     allow_methods=["*"],   # allow POST, GET, OPTIONS, etc.
#     allow_headers=["*"],   # allow all headers
# )


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5500",
        "http://127.0.0.1:5500",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class PRRequest(BaseModel):
    pr_url: str


@app.post("/review-pr")
def review_pull_request(data: PRRequest):
    """
    Main endpoint:
    - Fetch PR diff from GitHub
    - Run multiple AI agents
    - Return a compressed review summary
    """

    # 1️⃣ Fetch GitHub PR diff (ScaleDown principle: diffs only)
    code_diff = fetch_pr_files(data.pr_url)

    # 2️⃣ Run agents
    static_result = static_review(code_diff)
    security_result = security_review(code_diff)
    style_result = style_review(code_diff)

    # 3️⃣ Combine agent outputs
    combined_review = f"""
STATIC ANALYSIS:
{static_result}

SECURITY REVIEW:
{security_result}

STYLE REVIEW:
{style_result}
"""

    # 4️⃣ Final compressed summary
    final_summary = summarize_review(combined_review)

    return {
        "pr_url": data.pr_url,
        "review": final_summary
    }

