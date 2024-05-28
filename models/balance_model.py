from connect_db import connect_db

conn, cursor = connect_db()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS balance (
        User_id INTEGER PRIMARY KEY AUTOINCREMENT,
        Amount REAL,
        Time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
''')

conn.commit()
conn.close()
