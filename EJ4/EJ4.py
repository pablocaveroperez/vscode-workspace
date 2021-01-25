import sqlite3

# Crear conexión 
conn = sqlite3.connect('mydatabase.db')

# Obtener cursor 
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS employees(id integer PRIMARY KEY, name text, salary real)") 
conn.commit()

cursor.execute("INSERT INTO employees VALUES(1, 'MANUEL', 700)") 
conn.commit()

cursor.execute("INSERT INTO EMPLOYEES VALUES(2, 'JOSE', 800)")
conn.commit()
cursor.execute("INSERT INTO EMPLOYEES VALUES(3, 'ANTONIO', 1500)")
conn.commit()

cursor.execute('SELECT SUM(salary) FROM EMPLOYEES')
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
