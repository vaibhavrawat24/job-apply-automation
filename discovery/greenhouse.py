import requests


def fetch_greenhouse(board):

    url = f"https://boards-api.greenhouse.io/v1/boards/{board}/jobs?content=true"

    try:
        res = requests.get(url)

        if res.status_code != 200:
            print("❌ Status:", res.status_code)
            return []

        data = res.json()

        jobs = data.get("jobs", [])

        print("Fetched:", len(jobs), "jobs from", board)

        parsed = []
        for j in jobs:
            parsed.append({
                "title": j["title"],
                "url": j["absolute_url"],
                "company": board,
                "source": "greenhouse",
                "description": j.get("content", "")
            })

        return parsed

    except Exception as e:
        print("❌ Fetch error:", e)
        return []