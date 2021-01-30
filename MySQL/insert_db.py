import mysql.connector

SQuery = "INSERT INTO example (id,data) VALUES ('9','dato');"
con = mysql.connector.connect(user="root", password="Reconamor1@", host="127.0.0.1", database="dbpython")
cursor = con.cursor()

cursor.execute(SQuery)
con.commit() #make sure data is stored
con.close()