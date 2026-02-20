from discovery.greenhouse import fetch_greenhouse


BOARDS = [
    "airtable",
    "stripe",
    "notion",
    "figma",
    "databricks",
    "openai",
    "discord",
    "coinbase",
    "brex",
    "scaleai",
    "rippling",
    "segment",
    "robinhood",
    "instacart",
    "plaid",
    "affirm",
    "asana",
    "loom",
]


def run():
    all_jobs = []

    for b in BOARDS:
        print("Checking:", b)
        all_jobs.extend(fetch_greenhouse(b))

    print("TOTAL JOBS:", len(all_jobs))
    return all_jobs