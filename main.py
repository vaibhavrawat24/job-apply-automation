from discovery.run_discovery import run as run_discovery
from apply.router import route_apply
from relevance.run_filter import run as run_filter

def main():
    jobs = run_discovery()
    jobs = run_filter(jobs)
    print("Jobs to apply:", len(jobs))

    for job in jobs:
        print(job.get("title"), "->", job.get("url"))
        print(jobs[0].keys())

    # for job in jobs:
    #     route_apply(job)

if __name__ == "__main__":
    main()