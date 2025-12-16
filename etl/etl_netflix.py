import psycopg2
import os
from dotenv import load_dotenv

# =========================================================
# CONFIG
# =========================================================
load_dotenv()

DB_URL = os.getenv("DATABASE_URL") or os.getenv("NEON_DB_URL")

# MAX_ROWS = None        # None = process all rows
MAX_ROWS = 10       # Uncomment for testing

# =========================================================
# HELPERS
# =========================================================

def get_or_create(cursor, table, column, value):
    cursor.execute(
        f"SELECT {table}_id FROM {table} WHERE {column} = %s",
        (value,)
    )
    row = cursor.fetchone()
    if row:
        return row[0]

    cursor.execute(
        f"INSERT INTO {table} ({column}) VALUES (%s) RETURNING {table}_id",
        (value,)
    )
    return cursor.fetchone()[0]


def parse_duration(duration):
    if not duration:
        return None, None

    parts = duration.split()
    if len(parts) >= 2:
        try:
            value = int(parts[0])
            unit = parts[1].lower()
            if "season" in unit:
                return value, "season" if value == 1 else "seasons"
            return value, "min"
        except Exception:
            return None, None

    return None, None


# =========================================================
# MAIN ETL
# =========================================================

def main():
    print("Starting ETL...")

    conn = psycopg2.connect(DB_URL, sslmode="require")
    conn.autocommit = False
    cur = conn.cursor()

    # -----------------------------------------------------
    # Fetch data with optional LIMIT
    # -----------------------------------------------------

    if MAX_ROWS is not None:
        cur.execute("SELECT * FROM netflix_shows LIMIT %s", (MAX_ROWS,))
        print(f"Processing {MAX_ROWS} rows")
    else:
        cur.execute("SELECT * FROM netflix_shows")
        print("Processing all rows")

    rows = cur.fetchall()

    # -----------------------------------------------------
    # ETL loop
    # -----------------------------------------------------

    for row in rows:
        (
            show_id, type_, title, director, cast_members,
            country, date_added, release_year,
            rating, duration, listed_in, description
        ) = row

        # -------- TYPE --------
        if not type_:
            continue

        cur.execute(
            "SELECT type_id FROM show_type WHERE type_name = %s",
            (type_,)
        )
        type_row = cur.fetchone()
        if not type_row:
            continue
        type_id = type_row[0]

        # -------- RATING --------
        rating_id = None
        if rating:
            cur.execute(
                "SELECT rating_id FROM rating WHERE rating_code = %s",
                (rating,)
            )
            rating_row = cur.fetchone()
            if rating_row:
                rating_id = rating_row[0]

        duration_value, duration_unit = parse_duration(duration)

        # -------- SHOW --------
        cur.execute("""
            INSERT INTO show (
                show_id, title, type_id, rating_id,
                release_year, date_added,
                duration_value, duration_unit, description
            )
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
            ON CONFLICT (show_id) DO NOTHING
        """, (
            show_id, title, type_id, rating_id,
            release_year, date_added,
            duration_value, duration_unit, description
        ))

        # -------- DIRECTOR --------
        if director:
            for name in director.split(","):
                name = name.strip()
                if name:
                    person_id = get_or_create(cur, "person", "full_name", name)
                    cur.execute("""
                        INSERT INTO show_person (show_id, person_id, role)
                        VALUES (%s,%s,'Director')
                        ON CONFLICT DO NOTHING
                    """, (show_id, person_id))

        # -------- CAST --------
        if cast_members:
            for name in cast_members.split(","):
                name = name.strip()
                if name:
                    person_id = get_or_create(cur, "person", "full_name", name)
                    cur.execute("""
                        INSERT INTO show_person (show_id, person_id, role)
                        VALUES (%s,%s,'Cast')
                        ON CONFLICT DO NOTHING
                    """, (show_id, person_id))

        # -------- COUNTRY --------
        if country:
            for c in country.split(","):
                c = c.strip()
                if c:
                    country_id = get_or_create(cur, "country", "country_name", c)
                    cur.execute("""
                        INSERT INTO show_country (show_id, country_id)
                        VALUES (%s,%s)
                        ON CONFLICT DO NOTHING
                    """, (show_id, country_id))

        # -------- GENRE --------
        if listed_in:
            for g in listed_in.split(","):
                g = g.strip()
                if g:
                    genre_id = get_or_create(cur, "genre", "genre_name", g)
                    cur.execute("""
                        INSERT INTO show_genre (show_id, genre_id)
                        VALUES (%s,%s)
                        ON CONFLICT DO NOTHING
                    """, (show_id, genre_id))

    conn.commit()
    cur.close()
    conn.close()

    print("ETL completed successfully")


# =========================================================
# ENTRY POINT
# =========================================================

if __name__ == "__main__":
    main()
