from conect_db import conect_db

conn, cursor = conect_db()

conect_db.execute('''
    CREATE TABLE IF NOT EXISTS balance (
        User_id INTEGER PRIMARY KEY AUTOINCREMENT,
        Amount REAL,
        Time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
''')

conn.commit()
conn.close()
