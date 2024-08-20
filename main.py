from user_operations import add_user, fetch_user, fetch_all_users
from author_operations import add_author, fetch_author, fetch_all_authors
from book_operations import add_book, fetch_all_books, borrow_book, find_book, return_book
import os
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def library_system():
    clear()
    while True:
        action = input('''
Welcome to the Library Management System with Database Integration!
****
Main Menu:                       
1 - Book Operations
2 - User Operations
3 - Author Operations
4 - Quit
''')
        
        if action == '1':
            clear()
            while True:
                book_action = input('''
Welcome to the User Menu!
****
User Menu:                       
1 - Add a new book
2 - Borrow a book
3 - Return a book
4 - Search for a book
5 - Display all books
6 - Return to Main Menu
''')
                if book_action == '1':
                    clear()
                    add_book() 
                elif book_action == '2':
                    clear()
                    borrow_book()  
                elif book_action == '3':
                    clear()
                    return_book()  
                elif book_action == '4':
                    clear()
                    find_book() 
                elif book_action == '5':
                    clear()
                    fetch_all_books()
                elif book_action == '6':
                    library_system()
        elif action == '2':
            clear()
            while True:
                user_action = input('''
Welcome to the User Menu!
****
User Menu:                       
1 - Add a new user
2 - View user details
3 - Display all users
4 - Return to Main Menu
''')
                if user_action == '1':
                    clear()
                    add_user()
                elif user_action == '2':
                    clear()
                    fetch_user() 
                elif user_action == '3':
                    clear()
                    fetch_all_users() 
                elif user_action == '4':
                    library_system()

        elif action == '3':
            clear()
            while True:
                author_action = input('''
Welcome to the Author Menu!
****
Author Menu:                       
1 - Add a new author
2 - View author details
3 - Display all authors
4 - Return to Main Menu
''')
                if author_action == '1':
                    clear()
                    add_author() 
                elif author_action == '2':
                    clear()
                    fetch_author() 
                elif author_action == '3':
                    clear()
                    fetch_all_authors()
                elif author_action == '4':
                    library_system() 
        elif action == '4':
            break
        

library_system()