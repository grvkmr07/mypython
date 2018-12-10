import sqlite3
con = sqlite3.connect("mydb.db")
cursor = con.cursor()
cursor = cursor.execute("select * from company")
for row in cursor:
    print(row[0], row[1])
con.close()
