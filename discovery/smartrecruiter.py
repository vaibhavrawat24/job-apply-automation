import requests


def fetch_smartrecruiters(company):
    url = f"https://api.smartrecruiters.com/v1/companies/{company}/postings"

    try:
        res = requests.get(url, timeout=10)

        if res.status_code != 200:
            print("❌ SmartRecruiters status:", res.status_code)
            return []

        data = res.json()
        postings = data.get("content", [])

        jobs = []

        for j in postings:
            jobs.append({
                "title": j.get("name"),
                "url": j.get("ref"),
                "company": company,
                "location": j.get("location", {}).get("city"),
                "description": "",
                "source": "smartrecruiters"
            })

        print("Fetched:", len(jobs), "jobs from", company)
        return jobs

    except Exception as e:
        print("❌ SmartRecruiters error:", e)
        return []