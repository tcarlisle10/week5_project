import mysql.connector
from mysql.connector import Error



def connect_db():

    
    db_name = 'library_system'
    user = 'root' 
    password = 'Migmaster10!'
    host = '127.0.0.1' 

    

    try:
        conn = mysql.connector.connect(
            database = db_name, 
            user = user,
            password = password,
            host = host
        )

        if conn.is_connected():
            print("Connection to MYSQL database successful!")
            return conn


    except Error as e:
        print(f"Error: {e}")
        return None