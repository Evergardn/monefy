import sqlite3

def connect_db():
    conn = sqlite3.connect('cash.db')
    cursor = conn.cursor()
    return conn, cursor