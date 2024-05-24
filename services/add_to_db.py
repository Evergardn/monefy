import sqlite3
from datetime import datetime
from models.connect_db import connect_db

def add_data_to_db(user_id, amount):
    conn, cursor = connect_db()
    time = datetime.now()
    try:
        cursor.execute('INSERT INTO balance (User_id, Amount, Time) VALUES (?, ?, ?)', (user_id, amount, time))
        print('Inserted')
    except sqlite3.DatabaseError as e:
        cursor.execute('UPDATE balance SET Amount = ?, Time = ? WHERE User_id = ?', (amount, time, user_id))
        print('Updated')
    conn.commit()
    conn.close()

