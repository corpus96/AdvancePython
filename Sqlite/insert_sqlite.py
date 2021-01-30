import sqlite3;

con = sqlite3.connect('pythondb.sqlite')
query = "INSERT INTO usuarios ('nombre', 'tipo', 'edad') VALUES ('John', 'Normal', 99)"


con.execute(query)
con.commit()
con.close()