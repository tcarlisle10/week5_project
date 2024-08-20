from db_connection import connect_db, Error

def add_author():
    conn = connect_db()

    if conn is not None:
        try:
            cursor = conn.cursor()

            name = input("What is Author's full name? ").title()
            books_written = int(input("How many books has the Author wrote? "))
            awards = int(input("How many awards does this Author have? "))
            

            new_user = (name, books_written, awards)

            query = "INSERT INTO authors (author_name, books_written, awards) VALUES (%s, %s, %s);"

            cursor.execute(query, new_user)
            conn.commit() 
            print(f"New author {name} added successfully")

        except Error as e:
            print(f"Error: {e}")

        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()

if __name__ == "__main__":
    add_author()


#----------------------------------------------------------------#

def fetch_author():
    conn = connect_db()

    if conn is not None:
        try:
            authors_id = input("What is the id of the author you're looking for? ")
            cursor = conn.cursor()

            query = "SELECT * FROM authors WHERE id = %s;"

            cursor.execute(query, (authors_id,)) 

            
            id, name, books_num, awards = cursor.fetchone()
            print(f"{id}: {name}, Books written: {books_num}, Awards: {awards}")

        except Error as e:
            print(f"Error: {e}")

        finally:
            cursor.close()
            conn.close()

if __name__ == "__main__":
    fetch_author()

#------------------------------------------------------#

def fetch_all_authors():
    conn = connect_db()

    if conn is not None:
        try:

            cursor = conn.cursor()

            
            query = 'SELECT * FROM authors;'

            
            cursor.execute(query)

            for id, name, books_written, awards in cursor.fetchall():
                print(f"{id}: {name}, Books written: {books_written}, Awards: {awards}")

    
        except Error as e:
            print(f"Error: {e}")

        finally:
            cursor.close()
            conn.close() # NEVER FORGET
            print("Connection successfully close")

if __name__ == "__main__":
    fetch_all_authors()