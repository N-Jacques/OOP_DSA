import getpass
import sqlite3
import time
from colorama import Fore, Style, init

db_path = "./database/data.db"  # Path to your database file
user_data = sqlite3.connect(db_path)  # Connect to the database

init(autoreset=True) # Initialize colorama

def signup():
    print(Fore.GREEN + "=" * 49)
    print("")
    print(Fore.YELLOW + "███████╗██╗ ██████╗ ███╗   ██╗    ██╗   ██╗██████╗ ")
    print(Fore.YELLOW + "██╔════╝██║██╔════╝ ████╗  ██║    ██║   ██║██╔══██╗")
    print(Fore.YELLOW + "███████╗██║██║  ███╗██╔██╗ ██║    ██║   ██║██████╔╝")
    print(Fore.YELLOW + "╚════██║██║██║   ██║██║╚██╗██║    ██║   ██║██╔═══╝ ")
    print(Fore.YELLOW + "███████║██║╚██████╔╝██║ ╚████║    ╚██████╔╝██║     ")
    print(Fore.YELLOW + "╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝     ╚═════╝ ╚═╝     ")
    print("")
    print(Fore.GREEN + "=" * 49)
    print("")
    print("Type '/' at any time to go back to the main menu.\n")

    cursor = None  # Initialize cursor to None to avoid reference error in the finally block
    
    try:
        while True:
            while True:
                signup_fname = input("Enter your First Name: ").strip()
                if signup_fname.lower() == '/':
                    print("Returning to Main Menu...")
                    time.sleep(1.5)
                    return
                if not signup_fname:  # Check if the input is blank
                    print(Fore.RED + Style.BRIGHT + "Error: First name cannot be blank.\n")
                else:
                    break  # Valid input

            while True:
                signup_lname = input("Enter your Last Name: ").strip()
                if signup_lname.lower() == '/':
                    print("Returning to Main Menu...")
                    time.sleep(1.5)
                    return
                if not signup_lname:  # Check if the input is blank
                    print(Fore.RED + Style.BRIGHT + "Error: Last name cannot be blank.\n")
                else:
                    break  # Valid input

            while True:
                signup_user = input("Enter New Username: ").strip()
                if signup_user.lower() == '/':
                    print("Returning to Main Menu...")
                    time.sleep(1.5)
                    return

                if not signup_user:  # Check if the input is blank
                    print(Fore.RED + Style.BRIGHT + "Error: Username cannot be blank.\n")
                    continue  # Restart the loop for another attempt

                # Check if username already exists
                cursor = user_data.cursor()
                query = "SELECT * FROM User WHERE username = ?"
                cursor.execute(query, (signup_user,))
                result = cursor.fetchone()

                if result:  # If username exists
                    print(Fore.RED + Style.BRIGHT + "Error: Username already taken. Please choose a different username.\n")
                else:
                    break  # Valid input and username is available
                    
            while True:
                signup_pass = getpass.getpass("Enter Password: ")
                if signup_pass.lower() == '/':
                    print("Returning to Main Menu...")
                    time.sleep(1.5)
                    return
                if not signup_pass:  # Check if the input is blank
                    print(Fore.RED + Style.BRIGHT + "Error: Password cannot be blank.\n")
                else:
                    break  # Valid input
        
            while True:
                signup_phone = input("Enter Phone number (09xxxxxxxxx): ")
                if signup_phone.lower() == '/':
                    print("Returning to Main Menu...")
                    time.sleep(1.5)
                    return
                if not signup_phone:  # Check if the input is blank
                    print(Fore.RED + Style.BRIGHT + "Error: Phone number cannot be blank.\n")
                else:
                    break  # Valid input
            
            while True:
                signup_address = input("Enter your address (ex. 123 Tigasin St. Tondo, Manila): ")
                if signup_address.lower() == '/':
                    print("Returning to Main Menu...")
                    time.sleep(1.5)
                    return
                if not signup_address:  # Check if the input is blank
                    print(Fore.RED + Style.BRIGHT + "Error: Address cannot be blank.\n")
                else:
                    break  # Valid input
        
            # Insert user details into the User table
            cursor = user_data.cursor()
            insert_user_query = """
            INSERT INTO User (first_name, last_name, username, password, phone_number, address) 
            VALUES (?, ?, ?, ?, ?, ?)
            """
            cursor.execute(insert_user_query, (signup_fname, signup_lname, signup_user, signup_pass, signup_phone, signup_address))
            user_data.commit()

            print("\nSign up successful! Please log in.")
            time.sleep(2)
            break  # Successful sign-up; exit loop

    except sqlite3.Error as e:
        print(f"Database error: {e}")

    except KeyboardInterrupt:
        print("\nReturning to main menu...")

    finally:
        if cursor:
            cursor.close()  # Safe to close cursor
