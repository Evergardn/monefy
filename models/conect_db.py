import sqlite3

def conect_db():
    conn = sqlite3.connect('cash.db')
    cursor = conn.cursor()
    return conn, cursor