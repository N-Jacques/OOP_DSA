import os
import time
import sqlite3
from colorama import Fore, Style, init
import sys

from src.editProfile_page import editProfile  

db_path = "./database/data.db"
user_data = sqlite3.connect(db_path)  

def clear_screen(): #Clears the terminal screen.
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For macOS/Linux
        os.system('clear')

def verify_user(user_id):#Verify if the provided username exist in the database.
    try:
        cursor = user_data.cursor()
        query = "SELECT * FROM User WHERE user_id = ?"
        cursor.execute(query, (user_id))
        result = cursor.fetchone()
        return result is not None
    
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return False

def fetch_user_data(user_id):
        cursor = user_data.cursor()
        cursor.execute( # Query to retrieve user information TODO add "password" when implenting hide pass
            "SELECT user_id, username, first_name, last_name, password, address, phone_number FROM user WHERE user_id = ?", (user_id,)
        )  
        user = cursor.fetchone()  # Fetch row
        if user:
            return {
                "user_id": user[0],  # Include user_id here
                "username": user[1],
                "profile_name": f"{user[2]} {user[3]}",  # Combine first_name and last_name
                #"password": user[4], TODO remove comment logo when implenting count the char val of pass then convert to asterisk
                "address": user[5],
                "phone_number": user[6],
            }      
        else:
            print("User not found in the database.")
            time.sleep(2)
            clear_screen()
            return None       

def display_profile(user_id):#Displays user profile information.
        print("Accessing your profile...")
        time.sleep(1)
        print(Fore.GREEN + Style.BRIGHT +"=" * 40)
        print(f"Username: {user_id['username']}")
        print(f"Name: {user_id['profile_name']}")
        print("Password: **********")
        print(f"Address: {user_id['address']}")
        print(f"Phone number: {user_id['phone_number']}")
        print(Fore.GREEN + Style.BRIGHT +"=" * 40)

def profile_page(user_id):
    profile = fetch_user_data(user_id)  # Fetch user data using the ID

    while True:
        clear_screen()

        # header of home
        print(Fore.GREEN + "=" * 60)
        print("")
        print(Fore.YELLOW + Style.BRIGHT + "██████╗ ██████╗  ██████╗ ███████╗██╗██╗     ███████╗")
        print(Fore.YELLOW + Style.BRIGHT + "██╔══██╗██╔══██╗██╔═══██╗██╔════╝██║██║     ██╔════╝")
        print(Fore.YELLOW + Style.BRIGHT + "██████╔╝██████╔╝██║   ██║█████╗  ██║██║     █████╗  ")
        print(Fore.YELLOW + Style.BRIGHT + "██╔═══╝ ██╔══██╗██║   ██║██╔══╝  ██║██║     ██╔══╝  ")
        print(Fore.YELLOW + Style.BRIGHT + "██║     ██║  ██║╚██████╔╝██║     ██║███████╗███████ ")
        print(Fore.YELLOW + Style.BRIGHT + "╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝╚══════╝")
        print("")
        print(Fore.GREEN + "=" * 60)
        print("")

        display_profile(profile)
        print("1. Edit Profile")
        print("2. Order History")
        print("3. Log out")

        profile_choice = input("\nEnter your choice (1-3) / for back: ").strip()

        if profile_choice == "1":
            clear_screen()
            editProfile(profile)  # Pass the profile dictionary to editProfile
            profile = fetch_user_data(user_id)  # Reload profile after edits

        elif profile_choice == "2":
            from src.order_history import order_choice
            order_choice(user_id)
            time.sleep(0.5)

        elif profile_choice =="3":
             from src.startup_page import startup
             clear_screen()
             print("\nThank you for shopping with us! Logging out")
             time.sleep(0.5)
             startup()

        elif profile_choice == "/":
            print("Exiting Profile Page...")
            from src.home_page import home
            home(user_id)  # Pass the integer user_id
            break    

        else:
            print("Invalid choice! Please try again.")
            time.sleep(0.5)