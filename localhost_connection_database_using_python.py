#localhost_connection_database_using_python.py:
#Write a program to connect localhost and then create a database called as python_batch_5
import mysql.connector as MC
hostname='127.0.0.1'
username='root'
passwd=''
dbname='python_batch_52'
connection=MC.MySQLConnection(host=hostname,user=username,password=passwd)
if(connection):
    print("<<Localhost connected successfully>>")
    print("connection=",connection)
sql1="CREATE DATABASE "+dbname
cursor1=connection.cursor()
result1=cursor1.execute(sql1)
print(dbname,"Created successfully")
cursor1.close()#closing cursor object
connection.close() # closing connection with localhost
