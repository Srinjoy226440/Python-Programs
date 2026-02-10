#localhost_connection_using_python.py: Write a program to connect localhost
import mysql.connector as MC
hostname='127.0.0.1'
username='root'
passwd=''
connection=MC.MySQLConnection(host=hostname,user=username,password=passwd)
if(connection):
    print("<<Localhost connected successfully>>")
    print("connection=",connection)
connection.close() # closing connection with localhost
