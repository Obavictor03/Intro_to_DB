import mysql.connector
from mysql.connector import Error

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Oba.Victor11"
)

if mydb.is_connected():
    cursor = mydb.cursor()

    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

    print("Database 'alx_book_store' created successfully!")
else:
    print(Error)

cursor.close()
mydb.close()