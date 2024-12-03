import getpass
from src.home_page import home
import sqlite3
import time
from colorama import Fore, Style, init

db_path = "./database/data.db"  # Correct path to the database file
user_data = sqlite3.connect(db_path)  # Now using the actual path to connect

init(autoreset=True) # Initialize colorama

def verify_user(username, password): # Verify if the provided username and password exist in the database.
    cursor = user_data.cursor() # Object to interact with database
    query = "SELECT * FROM User WHERE username = ? AND password = ?" # SQL syntax to check if input exists 
    cursor.execute(query, (username, password)) # SQL query of the input username and password
    result = cursor.fetchone() # Fetch first matching record 
    return result is not None  # True if a matching record is found, False otherwise

def login():
    # Print the improved banner with color and ASCII art for "Login"
    print(Fore.GREEN + "=" * 39)
    print("")
    print(Fore.YELLOW + "██╗      ██████╗  ██████╗ ██╗███╗   ██╗")
    print(Fore.YELLOW + "██║     ██╔═══██╗██╔════╝ ██║████╗  ██║")
    print(Fore.YELLOW + "██║     ██║   ██║██║  ███╗██║██╔██╗ ██║")
    print(Fore.YELLOW + "██║     ██║   ██║██║   ██║██║██║╚██╗██║")
    print(Fore.YELLOW + "███████╗╚██████╔╝╚██████╔╝██║██║ ╚████║")
    print(Fore.YELLOW + "╚══════╝ ╚═════╝  ╚═════╝ ╚═╝╚═╝  ╚═══╝")
    print("")
    print(Fore.GREEN + "=" * 39)
    print("\n" + Style.BRIGHT + "Type '/' at any time to go back to the main menu.\n")


    try:
        while True:
            login_user = input("Enter username: ")
            if login_user.lower() == '/': # if "/" is inputted, return
                print("Returning to Main Menu...")
                time.sleep(1.5)
                return  # Exit function

            # Get password securely
            login_pass = getpass.getpass("Enter password: ") # Hide password when typing 
            if login_pass.lower() == '/':
                print("Returning to Main Menu...")
                time.sleep(1.5)
                return  # Exit function

            # Verify credentials
            if verify_user(login_user, login_pass):
                print("\n")
                print("Login successful, moving to Home...")
                print("\n")
                print(f"Welcome back, {login_user}!")
                time.sleep(1.5)
                home()  # Proceed to homepage only on successful login
                return  # Ensure function exits after proceeding
            else:
                print(Fore.RED + Style.BRIGHT + "Invalid username or password. Please try again.\n")

    except KeyboardInterrupt:
        print("\nReturning to main menu...")
        return

