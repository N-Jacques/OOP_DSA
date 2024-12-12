import os
import time
import sqlite3
from src.editProfile_page import editProfile  


db_path = "./database/data.db"

"""Clears the terminal screen."""
def clear_screen():
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For macOS/Linux
        os.system('clear')

try:
    user_data = sqlite3.connect(db_path)  

except sqlite3.Error as e: #error handling will print a message when database is not found instead crashing the entire program
    print(f"Database connection error: {e}")
    exit(1)


"""Verify if the provided username exist in the database."""
def verify_user(username):

    try:
        cursor = user_data.cursor()
        
        query = "SELECT * FROM User WHERE username = ? and password "
        cursor.execute(query, (username))
        result = cursor.fetchone()
        return result is not None
    
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return False


"""Fetches user data from the database."""
def fetch_user_data(username):
    try:
        cursor = user_data.cursor()
        # Query to retrieve user information
        cursor.execute(
            "SELECT first_name, last_name, password, address_id FROM user WHERE username = ?",(username,))
        
        user = cursor.fetchone()

        if user:
            return {
                "username": username,
                "profile_name": f"{user[0]} {user[1]}",  # Combine first_name and last_name
                "password": user[2],
                "address_id": user[3],
            }
        
        else:
            print("User not found in the database.")
            time.sleep(2)
            clear_screen()
            return None
        
    except sqlite3.Error as error:
        print(f"Database error: {error}. Loading default profile.")
        return None

"""Displays user profile information."""
def display_profile(profile):

    try:

        print("Accessing your profile...")

        time.sleep(1)

        print("=" * 40)
        print(f"Username: {profile['username']}")
        print(f"Name: {profile['profile_name']}")
        print(f"Password: {profile['password']}")
        print(f"Address ID: {profile['address_id']}")
        print("=" * 40)

    except KeyError as error:
        print(f"Error displaying profile: Missing {error}")



def profile_page(username):
    profile = fetch_user_data(username)

    if not profile:
        print("Profile not found. Returning to the homepage.")
        time.sleep(2)
        return

    while True:
        clear_screen()
        display_profile(profile)

        print("1. Edit Profile")
        print("2. Order History")
        print("3. Exit Profile Page")

        profile_choice = input("\nEnter your choice (1-3): ").strip()

        if profile_choice == "1":
            clear_screen()
            editProfile(profile)
            profile = fetch_user_data(profile["username"])  # Reload profile to reflect changes

        elif profile_choice == "2":
            try:
                from src.order_history import order_choice
                order_choice()
            except ImportError:
                print("Order history functionality is unavailable.")
            time.sleep(1)

        elif profile_choice == "3":
            print("Exiting Profile Page...")
            try:
                from src.home_page import home
                home(username)
            except ImportError:
                print("Homepage functionality is unavailable.")
            break

        else:
            print("Invalid choice! Please try again.")
            time.sleep(1)