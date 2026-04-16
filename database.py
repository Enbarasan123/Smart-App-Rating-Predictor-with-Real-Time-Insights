import sqlite3

def init_db():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()

    c.execute("""
        CREATE TABLE IF NOT EXISTS predictions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            app_name TEXT,
            reviews INTEGER,
            installs INTEGER,
            price REAL,
            prediction REAL
        )
    """)

    conn.commit()
    conn.close()


def save_prediction(app_name, reviews, installs, price, prediction):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()

    c.execute("""
        INSERT INTO predictions (app_name, reviews, installs, price, prediction)
        VALUES (?, ?, ?, ?, ?)
    """, (app_name, reviews, installs, price, prediction))

    conn.commit()
    conn.close()