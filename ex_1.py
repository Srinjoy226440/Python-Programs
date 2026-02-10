# create_database_and_table.py
import mysql.connector as MC

hostname = '127.0.0.1'
username = 'root'
passwd = ''
dbname = 'pythonexam'
tablename = 'marks'

# Step 1: Connect without database to create pythonexam
connection = MC.MySQLConnection(host=hostname, user=username, password=passwd)
cursor1 = connection.cursor()
cursor1.execute(f"CREATE DATABASE IF NOT EXISTS {dbname}")
print(f"<<Database {dbname} created successfully (if not existed)>>")
cursor1.close()
connection.close()

# Step 2: Reconnect to pythonexam and create table marks
connection = MC.MySQLConnection(host=hostname, user=username, password=passwd, database=dbname)
cursor1 = connection.cursor()

sql_create = f"""
CREATE TABLE IF NOT EXISTS {tablename} (
    roll INT(3) PRIMARY KEY,
    name VARCHAR(25),
    p1 INT(3),
    p2 INT(3),
    total INT(3),
    avg INT(3)
)
"""
cursor1.execute(sql_create)
print(f"<<Table {tablename} created successfully (if not existed)>>")

cursor1.close()
connection.close()
