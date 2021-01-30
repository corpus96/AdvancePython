import mysql.connector

SQuery = "CREATE TABLE example (id INT, data VARCHAR(100));"
con = mysql.connector.connect(user="root", password="Reconamor1@", host="127.0.0.1", database="dbpython")
cursor = con.cursor()

cursor.execute(SQuery)
con.close()