from github import fetch_pr_files

pr_url = "https://github.com/octocat/Hello-World/pull/1"

code = fetch_pr_files(pr_url)
print(code[:1000])
