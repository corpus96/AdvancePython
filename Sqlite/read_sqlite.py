import sqlite3

con = sqlite3.connect('pythondb.sqlite')
query = "SELECT * FROM usuarios"
num = '1'
query_select_one = "SELECT * FROM usuarios WHERE id=?"

#fetch all/only one
for row in con.execute(query_select_one, num):
    print(row)

con.close()