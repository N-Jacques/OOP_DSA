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
                    
            signup_pass = getpass.getpass("Enter Password: ")
            if signup_pass.lower() == '/':
                print("Returning to Main Menu...")
                time.sleep(1.5)
                return
            
            signup_phone = input("Enter Phone number (09xxxxxxxxx): ")
            if signup_phone.lower() == '/':
                print("Returning to Main Menu...")
                time.sleep(1.5)
                return
            
            print("\nEnter your Address Details below: ")
            
            signup_street = input("Enter Street (Required): ")
            if signup_street.lower() == '/':
                print("Returning to Main Menu...")
                time.sleep(1.5)
                return

            signup_house = input("Enter House No. (Required): ")
            if signup_house.lower() == '/':
                print("Returning to Main Menu...")
                time.sleep(1.5)
                return
            
            signup_room = input("Enter Room No. (Leave empty if not applicable): ")
            if signup_room.lower() == '/':
                print("Returning to Main Menu...")
                time.sleep(1.5)
                return
            
            signup_city = input("Enter City (Required): ")
            if signup_city.lower() == '/':
                print("Returning to Main Menu...")
                time.sleep(1.5)
                return
            
            signup_region = input("Enter Region (Leave empty if not applicable): ")
            if signup_region.lower() == '/':
                print("Returning to Main Menu...")
                time.sleep(1.5)
                return
            
            signup_zip = input("Enter Zip Code (Leave empty if not applicable): ")
            if signup_zip.lower() == '/':
                print("Returning to Main Menu...")
                time.sleep(1.5)
                return
        
            # Insert user details into the User table
            cursor = user_data.cursor()
            insert_user_query = """
            INSERT INTO User (first_name, last_name, username, password, phone_number) 
            VALUES (?, ?, ?, ?, ?)
            """
            cursor.execute(insert_user_query, (signup_fname, signup_lname, signup_user, signup_pass, signup_phone))
            user_data.commit()

            # Insert address into the Address table
            insert_address_query = """
            INSERT INTO Address (street_name, house_number, room_number, city, region, zip_code) 
            VALUES (?, ?, ?, ?, ?, ?)
            """
            cursor.execute(insert_address_query, (signup_street, signup_house, signup_room or None, signup_city, signup_region or None, signup_zip or None))
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
