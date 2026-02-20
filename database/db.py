import sqlite3

DB = "database/jobs.db"


def save_job(job):
    conn = sqlite3.connect(DB)
    c = conn.cursor()

    try:
        c.execute(
            "INSERT INTO jobs(company,title,url) VALUES(?,?,?)",
            (job["company"], job["title"], job["url"])
        )
        conn.commit()
        print("Saved:", job["title"])
    except:
        pass

    conn.close()