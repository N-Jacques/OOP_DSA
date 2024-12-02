import os
import time
import sqlite3
from src.editProfile_page import editProfile

db_path = "./database/data.db"  # Path to your database file
user_data = sqlite3.connect(db_path)  # Now using the actual path to connect


def clear_screen(): #clears screen
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')



# Function to fetch user data from the database
def fetch_user_data(username):
    """Fetches user data from the database."""
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Query to retrieve user information
        cursor.execute("SELECT first_name, last_name, password, address_id FROM user WHERE username = ?", (username,))
        user = cursor.fetchone()

        # Check if user exists in the database
        if user:
            return {
                "username": username,  # Use the input username for consistency
                "profile_name": f"{user[0]} {user[1]}",  # Combine first_name and last_name
                "password": user[2],
                "address_id": user[3],
            }
        else:
            print("User not found in the database. Loading default profile.")
            time.sleep(2)
            clear_screen()

    except sqlite3.Error as error:
        print(f"Database error: {error}")
        return {
            "username": "default_user",
            "profile_name": "Default Name",
            "password": "default_password",
            "address": "default_address",
        }
    finally:
        conn.close()


# Initialize profile dictionary with default values
profile = {
    "username": "default_user",
    "profile_name": "Default Name",
    "password": "default_password",
    "address": "default_address",
}


def display_profile():
    """Displays user profile information and order history."""
    global profile
    profile = fetch_user_data(profile["username"])  # Refresh profile data from database

    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        """Query to fetch the order count for the user
        cursor.execute("SELECT COUNT(*) FROM orders WHERE username = ?", (profile["username"],))
        result = cursor.fetchone()
        order_count = result[0] if result else 0"""""


    except sqlite3.Error :
        print()
    finally:
        conn.close()


def profile_page():
    """Provides options to view, edit, or exit the profile."""
    while True:
        print("\nProfile Page:")
        print("1. Display Profile")
        print("2. Edit Profile")
        print("3. Exit Profile Page")

        profile_choice = input("\nEnter your choice (1-3): ").strip()
        clear_screen()

        if profile_choice == "1":
            display_profile()  # Show updated profile
        elif profile_choice == "2":
            editProfile(profile)  # Pass the profile dictionary for editing
        elif profile_choice == "3":
            print("Exiting Profile Page...")
            from src.home_page import home
            home()
            break
        else:
            print("ERROR! TRY AGAIN.\n")