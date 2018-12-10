import sqlite3
conn = sqlite3.connect('test1.db')
p = input("Enter table Name: ")
conn.execute('''CREATE TABLE IF NOT EXISTS P
            (NAME TEXT,
            CITY TEXT);''')
conn.close()
