from discovery.greenhouse import fetch_greenhouse
from discovery.lever import fetch_lever
from discovery.ashby import fetch_ashby
from discovery.workable import fetch_workable
from discovery.smartrecruiter import fetch_smartrecruiters

GREENHOUSE_BOARDS = ["airtable", "stripe"]
LEVER_BOARDS = ["welocalize","meesho"]
ASHBY_BOARDS = ["perplexity"]
WORKABLE = ["pandadoc","lyst", "testgorilla"]
SMART = ["pandadoc","lyst", "testgorilla"]

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

    for w in WORKABLE:
        print("Checking workable:", w)
        all_jobs.extend(fetch_workable(w))

    for s in SMART:
        print("Checking smartrecruiter:", s)
        all_jobs.extend(fetch_smartrecruiters(s))

    print("TOTAL JOBS:", len(all_jobs))
    return all_jobs