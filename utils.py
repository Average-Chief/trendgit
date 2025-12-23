def print_repos(repos):
    if not repos:
        print("😴 No repos found")
        return
    
    for idx, repo in enumerate(repos, start=1):
        name = repo["full_name"]
        desc = repo["description"] or "No Description"
        stars = repo["stargazers_count"]
        language = repo["language"] or "Unknown"

        print(f"""
            {idx}. 🚀 {name}
            ⭐ Stars     : {stars}
            🧠 Language  : {language}
            📄 Desc      : {desc}
        """)
