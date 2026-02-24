from discovery.greenhouse import fetch_greenhouse
from discovery.lever import fetch_lever
from discovery.ashby import fetch_ashby


GREENHOUSE_BOARDS = ["airtable", "stripe"]
LEVER_BOARDS = ["welocalize","meesho"]
ASHBY_BOARDS = [
    "perplexity",
]

def run():
    all_jobs = []

    for b in GREENHOUSE_BOARDS:
        print("Checking greenhouse:", b)
        all_jobs.extend(fetch_greenhouse(b))

    for b in LEVER_BOARDS:
        print("Checking lever:", b)
        all_jobs.extend(fetch_lever(b))

    for a in ASHBY_BOARDS:
        print("Checking ashby:", a)
        all_jobs.extend(fetch_ashby(a))

    print("TOTAL JOBS:", len(all_jobs))
    return all_jobs