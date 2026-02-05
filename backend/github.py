import requests
import os
from dotenv import load_dotenv

load_dotenv()

def parse_pr_url(pr_url):
    parts = pr_url.strip("/").split("/")
    owner = parts[3]
    repo = parts[4]
    pr_number = parts[6]
    return owner, repo, pr_number


def fetch_pr_files(pr_url):
    owner, repo, pr_number = parse_pr_url(pr_url)

    url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{pr_number}/files"
    headers = {
        "Authorization": f"token {os.getenv('GITHUB_TOKEN')}"
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise Exception("Failed to fetch PR files")

    files = response.json()

    patches = []
    for file in files:
        if file.get("patch"):
            patches.append(
                f"\nFILE: {file['filename']}\n{file['patch']}"
            )

    return "\n".join(patches)
