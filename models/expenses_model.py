from conect_db import conect_db

conn, cursor = conect_db()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS expenses (
        User_id INTEGER PRIMARY KEY AUTOINCREMENT,
        Type TEXT,
        Quantity REAL,
        Time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
''')

conn.commit()
conn.close()

