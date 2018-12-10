import sqlite3
import gksql1
import gksql
p = gksql.p
conn = sqlite3.connect('test1.db')

cursor = conn.execute("SELECT NAME, CITY FROM P")
for row in cursor:
    print("Name : ", row[0])
    print("City : ", row[1])


conn.close()
