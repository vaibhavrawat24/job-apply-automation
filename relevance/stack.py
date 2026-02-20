STACK = [
    "python",
    "javascript",
    "node",
    "react",
    "django",
    "flask",
    "C++",
    "CSS",
    "HTML",
    "Go",
    "MongoDB",
    "SQLite",
    "PostgreSQL",
    "Supabase",
    "Langchain",
    "llms",
    "ai",
    "machine learning",
    "REST API",
    "Linux",
    "Cloudrun", "Docker"
]


def has_stack(job):
    text = job.get("description", "").lower()

    for s in STACK:
        if s in text:
            return True

    return False