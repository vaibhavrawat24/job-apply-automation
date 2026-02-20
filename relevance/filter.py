KEYWORDS = [
    "software engineer",
    "software developer",
    "backend",
    "frontend",
    "full stack",
    "fullstack",
    "web engineer"
]

EXCLUDE_KEYWORDS = [
    "new grad",
    "new graduate",
    "graduate program",
    "graduate role",
    "campus",
    "university grad",
    "intern",
    "internship",
]

def is_relevant(job):
    title = job["title"].lower()

    for kw in EXCLUDE_KEYWORDS:
        if kw in title:
            return False

    for k in KEYWORDS:
        if k in title:
            return True

    return False