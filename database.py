import sqlite3

DB_PATH = "data/news.db"


def get_connection():
    return sqlite3.connect(DB_PATH)


def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS articles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            url TEXT UNIQUE NOT NULL,
            source TEXT NOT NULL,
            published TEXT,
            content TEXT,
            summary TEXT
        )
    """)

    conn.commit()
    conn.close()


def save_article(title, url, source, published, content, summary):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            INSERT INTO articles (title, url, source, published, content, summary)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (title, url, source, published, content, summary))

        conn.commit()
        return True

    except sqlite3.IntegrityError:
        return False

    finally:
        conn.close()