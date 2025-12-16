import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

DB_URL = os.getenv("DATABASE_URL") or os.getenv("NEON_DB_URL")

FILES_TO_APPLY = [
    "optimization.sql",
    "views.sql",
    "procedures.sql"
]

def main():
    if not DB_URL:
        print("Error: DATABASE_URL not found.")
        return

    conn = psycopg2.connect(DB_URL, sslmode="require")
    cur = conn.cursor()

    for filename in FILES_TO_APPLY:
        print(f"Applying {filename}...")
        try:
            with open(filename, "r", encoding="utf-8") as f:
                sql = f.read()
                cur.execute(sql)
                conn.commit()
                print(f"Successfully applied {filename}")
        except Exception as e:
            print(f"Error applying {filename}: {e}")
            conn.rollback()

    cur.close()
    conn.close()

if __name__ == "__main__":
    main()
