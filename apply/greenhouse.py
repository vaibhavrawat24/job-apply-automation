import requests

def apply_greenhouse(company):

    url = f"https://boards-api.greenhouse.io/v1/boards/{company}/jobs"
    print("CALLING:", url)

    try:
        res = requests.get(url, timeout=10)
        print("STATUS:", res.status_code)

        data = res.json()
        print("JSON KEYS:", data.keys())

        jobs = []

        for job in data.get("jobs", []):
            jobs.append({
                "company": company,
                "title": job.get("title"),
                "url": job.get("absolute_url"),
                "location": job.get("location", {}).get("name", "")
            })

        print(f"FOUND {len(jobs)} jobs for {company}")
        return jobs

    except Exception as e:
        print("Greenhouse error:", e)
        return []