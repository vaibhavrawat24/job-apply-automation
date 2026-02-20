import sqlite3

conn = sqlite3.connect("database/jobs.db")
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS jobs(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company TEXT,
    title TEXT,
    url TEXT UNIQUE,
    applied INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

conn.commit()
conn.close()

print("DB initialized")