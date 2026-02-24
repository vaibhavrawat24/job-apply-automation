import requests

def fetch_workable(subdomain):
    url = f"https://apply.workable.com/api/v1/widget/accounts/{subdomain}"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        res = requests.get(url, headers=headers, timeout=10)

        if res.status_code != 200:
            print(f"❌ Workable status: {res.status_code}")
            return []

        data = res.json()
        raw_jobs = data.get("jobs", [])

        jobs = []
        for j in raw_jobs:
            jobs.append({
                "title": j.get("title"),
                "url": j.get("url"),
                "company": subdomain,
                "location": j.get("location", {}).get("location_str", "Remote"),
                "source": "workable"
            })

        print(f"✅ Workable {subdomain}: {len(jobs)} jobs")
        return jobs

    except Exception as e:
        print(f"⚠️ Workable {subdomain} error: {e}")
        return []