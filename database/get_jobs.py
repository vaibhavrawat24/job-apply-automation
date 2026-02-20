import sqlite3

DB = "database/jobs.db"


def get_unapplied_jobs():
    conn = sqlite3.connect(DB)
    c = conn.cursor()

    rows = c.execute(
        "SELECT company,title,url FROM jobs WHERE applied=0"
    ).fetchall()

    conn.close()

    jobs = []
    for r in rows:
        jobs.append({
            "company": r[0],
            "title": r[1],
            "url": r[2]
        })

    return jobs