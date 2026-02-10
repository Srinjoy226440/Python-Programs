# insert_update_marks.py
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

# Insert records using user input
sql_insert = f"INSERT INTO {tablename}(roll, name, p1, p2, total, avg) VALUES (%s, %s, %s, %s, NULL, NULL)"
nrec = 0
while True:
    roll = int(input("Enter Roll number: "))
    name = input("Enter Name: ")
    p1 = int(input("Enter Marks in P1: "))
    p2 = int(input("Enter Marks in P2: "))
    val = (roll, name, p1, p2)
    cursor1.execute(sql_insert, val)
    nrec += 1
    print(f"Record inserted: ({roll}, {name}, {p1}, {p2})")
    choice = input("Do you want to enter more records (Y/N)? ")
    if choice.lower() != 'y':
        break

# Update total and avg
sql_update = f"UPDATE {tablename} SET total = p1+p2, avg = (p1+p2)/2"
cursor1.execute(sql_update)
print("<<Fields total and avg updated successfully!>>")

connection.commit()
print("Total number of records added =", nrec)

cursor1.close()
connection.close()
