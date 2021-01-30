import mysql.connector

SQuery = "SELECT * FROM example WHERE id=9"
con = mysql.connector.connect(user="root", password="Reconamor1@", host="127.0.0.1", database="dbpython")
cursor = con.cursor()

cursor.execute(SQuery)

rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.close()
con.close()