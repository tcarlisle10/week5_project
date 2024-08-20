import mysql.connector 
from mysql.connector import Error 

db_name = 'library_system'
user = 'root' 
password = 'Migmaster10!'
host = '127.0.0.1' 

# Establish our connection

try:
    conn = mysql.connector.connect(
        database = db_name, 
        user = user,
        password = password,
        host = host
    )

    if conn.is_connected():
        print("Connection to MYSQL database successful!")

    cursor = conn.cursor() # creating a cursor to act as a middle man between Python and MySQL

    query = 'SELECT * FROM books;'

    cursor.execute(query) # passing our query over to our cursor and executing it

    for row in cursor.fetchall():
        print(row)

except Error as e:
    print(f"Error: {e}")

finally:
    if conn and conn.is_connected():
        cursor.close()
        conn.close() #ALWAYS BE SURE TO CLOSE YOUR CONNECTIONS WHEN YOU'RE FINISHED WITH A QUERY
        print("Connection successfully closed")