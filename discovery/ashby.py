import requests


def fetch_ashby(company):
    url = f"https://api.ashbyhq.com/posting-api/job-board/{company}"

    try:
        res = requests.get(url, timeout=10)

        if res.status_code != 200:
            print("❌ Ashby status:", res.status_code)
            return []

        data = res.json()

        postings = data.get("jobs", [])

        jobs = []

        for j in postings:

            text_blob = " ".join([
                j.get("descriptionPlain", ""),
                j.get("responsibilitiesPlain", ""),
                j.get("requirementsPlain", "")
            ])

            jobs.append({
                "title": j.get("title"),
                "url": f"https://jobs.ashbyhq.com/{company}/{j.get('id')}",
                "company": company,
                "description": text_blob,
                "source": "ashby"
            })

        print("Fetched:", len(jobs), "jobs from", company)
        return jobs

    except Exception as e:
        print("❌ Ashby error:", e)
        return []