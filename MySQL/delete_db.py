import mysql.connector

SQuery = "DELETE FROM example WHERE id=9"
con = mysql.connector.connect(user="root", password="Reconamor1@", host="127.0.0.1", database="dbpython")
cursor = con.cursor()

cursor.execute(SQuery)
con.commit()

cursor.close()
con.close()
