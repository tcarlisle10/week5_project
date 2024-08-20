from db_connection import connect_db, Error

def add_user():
    conn = connect_db()

    if conn is not None:
        try:
            cursor = conn.cursor()

            name = input("What is your name? ").title()
            email = input("What is your email? ")
            phone = input("What is your phone number? ")
            address = input("What is your address? ")

            new_user = (name, email, address, phone)

            query = "INSERT INTO users (user_name, email, address, phone) VALUES (%s, %s, %s, %s);"

            cursor.execute(query, new_user)
            conn.commit() 
            print(f"New user {name} added successfully")

        except Error as e:
            print(f"Error: {e}")

        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()

if __name__ == "__main__":
    add_user()


#-----------------------------------------------------------------#

def fetch_user():
    conn = connect_db()

    if conn is not None:
        try:
            users_id = input("What is the id of the user you're looking for? ")
            cursor = conn.cursor()

            query = "SELECT * FROM users WHERE id = %s;"

            cursor.execute(query, (users_id,)) 

            
            id, name, email, phone, address = cursor.fetchone()
            print(f"{id}: {name}, {email}, {phone}, {address}")

        except Error as e:
            print(f"Error: {e}")

        finally:
            cursor.close()
            conn.close()

if __name__ == "__main__":
    fetch_user()

#====================================================================#

def fetch_all_users():
    conn = connect_db()

    if conn is not None:
        try:

            cursor = conn.cursor() 

            
            query = 'SELECT * FROM users;'

            
            cursor.execute(query)

            for id, name, email, phone, address in cursor.fetchall():
                print(f"{id}: {name}, {email}, {phone}, {address}")

    
        except Error as e:
            print(f"Error: {e}")

        finally:
            cursor.close()
            conn.close() 
            print("Connection successfully close")

if __name__ == "__main__":
    fetch_all_users()