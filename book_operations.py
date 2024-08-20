from db_connection import connect_db, Error

def add_book():
    conn = connect_db()

    if conn is not None:
        try:
            cursor = conn.cursor()

            title = input("What is the book name? ").title()
            author = input("Who is the Author of the book? ").title()
            isbn = int(input("What is the isbn number? "))
            pub_year = int(input("When was the publish year? "))

            new_book = (title, author, isbn, pub_year)

            query = "INSERT INTO books (title, author, isbn, publication_date) VALUES (%s, %s, %s, %s);"

            cursor.execute(query, new_book)
            conn.commit() 
            print(f"New book {title} added successfully")

        except Error as e:
            print(f"Error: {e}")

        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()

if __name__ == "__main__":
    add_book()

#-------------------------------------------------------------#

def fetch_all_books():
    conn = connect_db()

    if conn is not None:
        try:

            cursor = conn.cursor() 

            
            query = 'SELECT * FROM books;'

            
            cursor.execute(query)

            for id, title, author, isbn, publication_date, availability, author_id in cursor.fetchall():
                print(f"{id}: {title}, {author}, isbn: {isbn}, Publication year: {publication_date}, Available: {availability}, {author_id}")

    
        except Error as e:
            print(f"Error: {e}")

        finally:
            cursor.close()
            conn.close() 
            print("Connection successfully close")

if __name__ == "__main__":
    fetch_all_books()   

#------------------------------------------------------------------#

def borrow_book():
    conn = connect_db()

    if conn is not None:
        try:
            cursor = conn.cursor()

            

            book_id = input("What is the id of the book you're looking for? ")
            query = "SELECT * FROM books WHERE id = %s;"
            cursor.execute(query, (book_id,))
            

            id, title, author, isbn, publication_date, availability, author_id = cursor.fetchone()
            print(f"{id}: {title} by {author} {isbn} {publication_date} {availability} {author_id} has been checked out")

            remove_book(book_id)

        except Error as e:
            print(f"Error: {e}")

        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()

if __name__ == "__main__":
    borrow_book()





#---------------------------------------------------------#

def find_book():
    conn = connect_db()

    if conn is not None:
        try:
            book_id = input("What is the id of the book you're looking for? ")
            cursor = conn.cursor()
            query = "SELECT * FROM books WHERE id = %s;"
            cursor.execute(query, (book_id,))
            


            
            id, title, author, isbn, publication_date, availability, author_id = cursor.fetchone()
            print(f"{id}: {title}, {author}, {isbn}, {publication_date}, {availability}, {author_id}")

        except Error as e:
            print(f"Error: {e}")

        finally:
            cursor.close()
            conn.close()

if __name__ == "__main__":
    find_book()

#-----------------------------------------------------------#

def remove_book(book_id):
    conn = connect_db()

    if conn is not None:
        try:
            cursor = conn.cursor()

           
            query = "DELETE FROM books WHERE id = %s"
            cursor.execute(query, (book_id,))
            conn.commit()
            
            
            

            

        except Error as e:
            print(f"Error: {e}")

        finally:
            cursor.close()
            conn.close()

#-----------------------------------------------------------#

def return_book():
    conn = connect_db()

    if conn is not None:
        try:
            cursor = conn.cursor()

            title = input("What is the book name you are returning? ").title()
            author = input("Who is the Author of the book? ").title()
            isbn = int(input("What is the isbn number? "))
            pub_year = int(input("When was the publish year? "))

            returned_book = (title, author, isbn, pub_year)

            query = "INSERT INTO books (title, author, isbn, publication_date) VALUES (%s, %s, %s, %s);"

            cursor.execute(query, returned_book)
            conn.commit() 
            print(f"You have successfully returned: {title}")

        except Error as e:
            print(f"Error: {e}")

        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()

if __name__ == "__main__":
    return_book()