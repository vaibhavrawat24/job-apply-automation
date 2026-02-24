import requests


def fetch_lever(company):
    url = f"https://api.lever.co/v0/postings/{company}?mode=json"

    try:
        res = requests.get(url, timeout=10)

        if res.status_code != 200:
            print("❌ Lever status:", res.status_code)
            return []

        data = res.json()

        jobs = []
        for j in data:

            text_blob = " ".join([
                j.get("descriptionPlain", ""),
                j.get("additionalPlain", ""),
                j.get("listsPlain", "")
            ])

            jobs.append({
                "title": j.get("text"),
                "url": j.get("hostedUrl"),
                "company": company,
                "description": text_blob,
                "source": "lever"
            })

        print("Fetched:", len(jobs), "jobs from", company)
        return jobs

    except Exception as e:
        print("❌ Lever fetch error:", e)
        return []