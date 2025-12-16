import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

DB_URL = os.getenv("DATABASE_URL") or os.getenv("NEON_DB_URL")

def main():
    if not DB_URL:
        print("Error: DATABASE_URL not found.")
        return

    print(f"Connecting to DB...")
    # Try with sslmode=require first
    try:
        conn = psycopg2.connect(DB_URL, sslmode="require")
    except psycopg2.OperationalError:
        print("sslmode=require failed, trying sslmode=prefer")
        conn = psycopg2.connect(DB_URL, sslmode="prefer")

    cur = conn.cursor()
    
    print("Creating student table...")
    try:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS student (
                student_id SERIAL PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                year INT CHECK (year BETWEEN 1 AND 5),
                department TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT NOW()
            );
        """)
        conn.commit()
        print("Table 'student' created successfully.")
    except Exception as e:
        print(f"Error creating table: {e}")
        conn.rollback()
    
    cur.close()
    conn.close()

if __name__ == "__main__":
    main()
