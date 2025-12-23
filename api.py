import requests
from datetime import timedelta, datetime

url = "https://api.github.com/search/repositories"

def get_start_date(duration):
    now = datetime.utcnow()

    if duration=="day":
        return now-timedelta(days=1)
    if duration == "week":
        return now-timedelta(days=7)
    if duration == "month":
        return now-timedelta(days=30)
    if duration == "year":
        return now - timedelta(days=365)
    
def fetch_repos(duration,limit):
    start_date = get_start_date(duration).strftime("%Y-%m-%d")

    query = f"created:>{start_date}"
    
    params = {
        "q": query,
        "sort" :"stars",
        "order":"desc",
        "per_page":limit
    }

    response = requests.get(url,params=params,timeout=10)

    if response.status_code != 200:
        raise Exception(
        f"GitHub API error {response.status_code}: {response.json().get('message')}"
        )
    
    data = response.json()
    print("Fetched repos:", len(data.get("items", [])))
    return data.get("items",[])

