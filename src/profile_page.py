import os
import time
import sqlite3
from src.editProfile_page import editProfile

db_path = "./database/data.db"  # Path to your database file
user_data = sqlite3.connect(db_path)  # Now using the actual path to connect


# Default profile values
default_profile = {
    "username": "default_user",
    "profile_name": "Default Name",
    "password": "default_password",
    "address": "default_address",
}

def clear_screen():  # Clears the screen
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def verify_user(username, password): # Verify if the provided username and password exist in the database.
    cursor = user_data.cursor() # Object to interact with database
    query = "SELECT * FROM User WHERE username = ? AND password = ?" # SQL syntax to check if input exists 
    cursor.execute(query, (username, password)) # SQL query of the input username and password
    result = cursor.fetchone() # Fetch first matching record 
    return result is not None  # True if a matching record is found, False otherwise


# Initialize profile dictionary with default values
profile = default_profile.copy()

# Function to fetch user data from the database
def fetch_user_data(username):
    """Fetches user data from the database or defaults if the database is unavailable."""
    try:
        cursor = user_data.cursor()

        # Query to retrieve user information
        cursor.execute("SELECT first_name, last_name, password, address_id FROM user WHERE username = ?", (username,))
        user = cursor.fetchone()

        # Check if user exists in the database
        if user:
            return {
                "username": username,
                "profile_name": f"{user[0]} {user[1]}",  # Combine first_name and last_name
                "password": user[2],
                "address_id": user[3],
            }
        else:
            print("User not found in the database. Loading default profile.")
            time.sleep(2)
            clear_screen()
            return default_profile

    except sqlite3.Error as error:
        print(f"Database error: {error}. Loading default profile.")
        return default_profile  # Load default profile if any error occurs


def display_profile():
    """Displays user profile information and order history."""
    global profile
    profile = fetch_user_data(profile["username"])  # Refresh profile data from database or default

    try:
        cursor = user_data.cursor()

        print("Accessing your profile...")
        time.sleep(0.5)
        print("=" * 40)
        print(f"Username: {profile['username']}")
        print(f"Name: {profile['profile_name']}")
        print(f"Password: {profile['password']}")
        print(f"Address: {profile.get('address')}")
        print("=" * 40)

    except sqlite3.Error as error:


        print("=" * 40)
        print(f"Username: {profile['username']}")
        print(f"Name: {profile['profile_name']}")
        print(f"Password: {profile['password']}")
        print(f"Address: {profile.get('address', 'N/A')}")
        print("=" * 40)

def profile_page():
    """Provides options to view, edit, or exit the profile."""
    
    while True:

        display_profile()
        print("1. Edit Profile")
        print("2. Exit Profile Page")
        profile_choice = input("\nEnter your choice (1-3): ").strip()
        clear_screen()

        if profile_choice == "1":
            editProfile(profile)

        elif profile_choice == "2":
            print("Exiting Profile Page...")
            from src.home_page import home
            home()
            break

        else:
            print("ERROR! TRY AGAIN.\n")
