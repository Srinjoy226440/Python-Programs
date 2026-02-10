# display_marks.py
import mysql.connector as MC

hostname = '127.0.0.1'
username = 'root'
passwd = ''
dbname = 'pythonexam'
tablename = 'marks'

connection = MC.MySQLConnection(host=hostname, user=username, password=passwd, database=dbname)
if connection:
    print(f"<<Localhost {dbname} connected successfully>>")

cursor1 = connection.cursor()
sql_display = f"SELECT * FROM {tablename}"
cursor1.execute(sql_display)

print("Roll | Name       | P1  | P2  | Total | Avg")
print("-----+------------+-----+-----+-------+-----")
for row in cursor1.fetchall():
    print(row)

cursor1.close()
connection.close()
