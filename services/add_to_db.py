import sqlite3
from datetime import datetime
from models.connect_db import connect_db

def add_data_to_db(user_id, amount):
    conn, cursor = connect_db()
    time = datetime.now()
    expenses = check_expenses(user_id=2)
    try:
        cursor.execute('INSERT INTO balance (User_id, Amount, Time) VALUES (?, ?, ?)', (user_id, amount, time))
        print('Inserted')
    except sqlite3.DatabaseError:
        cursor.execute('UPDATE balance SET Amount = ?, Time = ? WHERE User_id = ?', (amount, time, user_id))
        print('Updated')
        print(check_expenses(user_id=2))
    conn.commit()
    conn.close()

def check_expenses(user_id):
    conn, cursor = connect_db()
    cursor.execute('SELECT Quantity FROM expenses WHERE User_id = ?', (user_id,))
    quantity = cursor.fetchone()[0]
    return quantity