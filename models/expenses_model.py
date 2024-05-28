from connect_db import connect_db

conn, cursor = connect_db()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS expenses (
        User_id INTEGER,
        Type TEXT,
        Quantity REAL,
        Time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
''')

conn.commit()
conn.close()

