import sqlite3
from datetime import datetime
from models.connect_db import connect_db

def remove_data_from_db(user_id, amount):
    conn, cursor = connect_db()
    time = datetime.now()
    try:
        cursor.execute('SELECT Amount FROM balance WHERE User_id = ?', (user_id,))
        current_amount = cursor.fetchone()
        
        if current_amount is not None:
            new_amount = current_amount[0] - amount
            cursor.execute('UPDATE balance SET Amount = ?, Time = ? WHERE User_id = ?', (new_amount, time, user_id))
            print('Updated (removed)')
        else:
            cursor.execute('INSERT INTO balance (User_id, Amount, Time) VALUES (?, ?, ?)', (user_id, amount, time))
            print('Inserted (removed)')
    except sqlite3.DatabaseError as e:
        print(f"Database error: {e}")
        raise

    conn.commit()
    conn.close()