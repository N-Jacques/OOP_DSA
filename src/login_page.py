import getpass
from src.home_page import homepage
import sqlite3
import keyboard

user_data = sqlite3.connect("db_path")  # Connect to the database
db_path = "./database/data.db"  # Relative path to your database file

def verify_user(username, password): # Verify if the provided username and password exist in the database.
    cursor = user_data.cursor()
    query = "SELECT * FROM user WHERE username = ? AND password = ?"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()
    return result is not None  # True if a matching record is found, False otherwise

def login():
    print("===========================")
    print("---------- Login ----------")
    print("===========================")
    print("\n")
    print("Type 'Esc' at any time to go back to the main menu.\n")

    try:
        while True:
            login_user = input("Enter username: ")
            if login_user.lower() == 'esc':
                print("Returning to Main Menu...")
                return
            
            # getpass for password hiding when input 
            login_pass = getpass.getpass("Enter password: ")
            if login_pass.lower() == 'esc':
                print("Returning to Main Menu...")
                return

            # Verify the user
            if verify_user(login_user, login_pass):
                print("Login successful, moving to Home...")
                print(f"Welcome back, {login_user}!")
                homepage()
                break  # Successful login; exit loop
            else:
                print("Invalid username or password. Please try again.\n")
    
    except KeyboardInterrupt:
        print("\nReturning to main menu...")
        return  

