import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("NEON_DB_URL")

def main():
    if not DATABASE_URL:
        raise RuntimeError("DATABASE_URL not set")
    conn = psycopg2.connect(DATABASE_URL, sslmode="require")
    cur = conn.cursor()
    cur.execute("SELECT current_database(), current_user;")
    db, user = cur.fetchone()

    print("Connected to PostgreSQL/NeonDB")
    print(f"Database: {db}, User: {user}")
    cur.close()
    conn.close()

if __name__ == "__main__":
    main()
