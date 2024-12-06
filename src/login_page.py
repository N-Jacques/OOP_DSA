import getpass
from src.home_page import home
import sqlite3
import time
from colorama import Fore, Style, init


db_path = "./database/data.db"  # relative path to database
user_data = sqlite3.connect(db_path)  # assign database to varable

init(autoreset=True) # Initialize colorama

def verify_user(username, password): # Verify if the provided username and password exist in the database.
    cursor = user_data.cursor() # Object to interact with database
    query = "SELECT user_id FROM User WHERE username = ? AND password = ?" # SQL syntax to check if input exists 
    cursor.execute(query, (username, password)) # SQL query of the input username and password
    result = cursor.fetchone() # Fetch first matching record 
    return result[0] if result else None  # True if a matching record is found, False otherwise

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
            if login_user.lower() == '/': # if "/" is inputted, go back
                print("Returning to Main Menu...")
                time.sleep(1.5)
                return 

            # Get password securely
            login_pass = getpass.getpass("Enter password: ") # Hide password when typing 
            if login_pass.lower() == '/':
                print("Returning to Main Menu...")
                time.sleep(1.5)
                return  

            # Verify credentials
            user_id = verify_user(login_user, login_pass)  # Get user_id if valid
            
            # login if correct details
            if user_id:
                print("\n")
                print("Login successful, moving to Home...")
                print("\n")
                print(f"Welcome back, {login_user}!")
                time.sleep(1.5)
                
                home(user_id)  
                return  
            else:
                print(Fore.RED + Style.BRIGHT + "Invalid username or password. Please try again.\n")

    except KeyboardInterrupt:
        print("\nReturning to main menu...")
        return

