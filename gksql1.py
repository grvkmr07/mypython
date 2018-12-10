import sqlite3
import gksql
p = gksql.p
conn = sqlite3.connect('test1.db')
cur = conn.cursor()
name = input("Enter name: ")
city = input("Enter city: ")
conn.execute('''INSERT INTO P(NAME, CITY) VALUES(?, ?)''', (name, city))
conn.commit()
conn.close()
