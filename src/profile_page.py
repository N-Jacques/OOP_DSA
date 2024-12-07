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
def verify_user(user_id):

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
    try:
        cursor = user_data.cursor()
        # Query to retrieve user information
        cursor.execute(
            "SELECT user_id, username, first_name, last_name, password, address_id, phone_number FROM user WHERE user_id = ?", (user_id,)
        )  
        user = cursor.fetchone()  # Fetch row
        if user:
            return {
                "user_id": user[0],  # Include user_id here
                "username": user[1],
                "profile_name": f"{user[2]} {user[3]}",  # Combine first_name and last_name
                "password": user[4],
                "address_id": user[5],
                "phone_number": user[6],
            }      
        else:
            print("User not found in the database.")
            time.sleep(2)
            clear_screen()
            return None       
    except sqlite3.Error as error:
        print(f"Database error: {error}. Loading default profile.")
        return None      
    except sqlite3.Error as error:
        print(f"Database error: {error}. Loading default profile.")
        return None

"""Displays user profile information."""
def display_profile(user_id):
        print("Accessing your profile...")
        time.sleep(1)
        print("=" * 40)
        print(f"Username: {user_id['username']}")
        print(f"Name: {user_id['profile_name']}")
        print(f"Password: {user_id['password']}")
        print(f"Address ID: {user_id['address_id']}")
        print(f"Phone number: {user_id['phone_number']}")
        print("=" * 40)

def profile_page(user_id):
    profile = fetch_user_data(user_id)  # Fetch user data using the ID

    while True:
        clear_screen()
        display_profile(profile)
        print("1. Edit Profile")
        print("2. Order History")
        print("3. Exit Profile Page")

        profile_choice = input("\nEnter your choice (1-3): ").strip()

        if profile_choice == "1":
            clear_screen()
            editProfile(profile)  # Pass the profile dictionary to editProfile
            profile = fetch_user_data(user_id)  # Reload profile after edits

        elif profile_choice == "2":

            from src.order_history import order_choice
            order_choice()
            time.sleep(1)

        elif profile_choice == "3":
            print("Exiting Profile Page...")
            from src.home_page import home
            home(user_id)  # Pass the integer user_id
           
            break

        else:
            print("Invalid choice! Please try again.")
            time.sleep(1)
