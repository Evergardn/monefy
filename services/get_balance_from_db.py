import sqlite3
from datetime import datetime
from models.connect_db import connect_db

def get_balance(user_id):
    conn, cursor = connect_db()
    cursor.execute('SELECT Amount FROM balance WHERE User_id = ?', (user_id,))
    amount = cursor.fetchone()[0]
    conn.close()
    return amount


