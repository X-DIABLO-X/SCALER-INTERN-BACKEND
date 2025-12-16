import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

DB_URL = os.getenv("DATABASE_URL") or os.getenv("NEON_DB_URL")

def main():
    if not DB_URL:
        print("Error: DATABASE_URL or NEON_DB_URL not found in environment.")
        return

    conn = psycopg2.connect(DB_URL, sslmode="require")
    cur = conn.cursor()

    print("Executing new_schema.sql...")
    try:
        with open("../new_schema.sql", "r", encoding='utf-8') as f:
            cur.execute(f.read())
    except FileNotFoundError:
        # Fallback if running from root
        with open("new_schema.sql", "r", encoding='utf-8') as f:
            cur.execute(f.read())
    
    print("Executing seed.sql...")
    try:
        with open("../seed.sql", "r", encoding='utf-8') as f:
            cur.execute(f.read())
    except FileNotFoundError:
        with open("seed.sql", "r", encoding='utf-8') as f:
            cur.execute(f.read())
    
    conn.commit()
    cur.close()
    conn.close()
    print("Database setup complete.")

if __name__ == "__main__":
    main()
