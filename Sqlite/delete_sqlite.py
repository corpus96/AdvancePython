import sqlite3

con = sqlite3.connect('pythondb.sqlite')
query = "DELETE FROM usuarios WHERE id=1"

con.execute(query)
con.commit()
con.close()