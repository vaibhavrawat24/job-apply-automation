from discovery.greenhouse import fetch_greenhouse
from discovery.lever import fetch_lever


GREENHOUSE_BOARDS = ["airtable", "stripe"]
LEVER_BOARDS = ["welocalize","meesho"]


def run():
    all_jobs = []

    for b in GREENHOUSE_BOARDS:
        print("Checking greenhouse:", b)
        all_jobs.extend(fetch_greenhouse(b))

    for b in LEVER_BOARDS:
        print("Checking lever:", b)
        all_jobs.extend(fetch_lever(b))

    print("TOTAL JOBS:", len(all_jobs))
    return all_jobs