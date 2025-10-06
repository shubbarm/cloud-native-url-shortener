import psycopg2
import os
import hashlib

from dotenv import load_dotenv
load_dotenv()

def get_db():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS"),
        dbname=os.getenv("DB_NAME"),
        port=5432,
        sslmode='require'
    )

def create_short_url(conn, url):
    short = hashlib.md5(url.encode()).hexdigest()[:6]
    with conn.cursor() as cur:
        cur.execute("INSERT INTO urls (short, original) VALUES (%s, %s) ON CONFLICT DO NOTHING", (short, url))
        conn.commit()
    return short

def get_original_url(conn, short):
    with conn.cursor() as cur:
        cur.execute("SELECT original FROM urls WHERE short = %s", (short,))
        result = cur.fetchone()
        return result[0] if result else None
