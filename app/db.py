import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

DB_URL = os.getenv("DATABASE_URL") or os.getenv("NEON_DB_URL")

def get_connection():
    return psycopg2.connect(DB_URL, sslmode="require")
