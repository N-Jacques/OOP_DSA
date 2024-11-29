import os
import time
from editProfile_page import editProfile


profile = {
    "username": "default_user",
    "profile_name": "Default Name",
    "password": "default_password",
    "address": "default_address"
}


def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def display_profile():
    print("Accessing your profile...")
    print()

    print("=" * 40)
    print(f"Username: {profile['username']}")
    print(f"Name: {profile['profile_name']}")
    print(f"Address: {profile['address']}")
    print(f"Password: {profile['password']}")
    print(f"Order History: 5 orders")
    print("=" * 40)

def profile_page():
    while True:
        
        print("\nProfile Page:")
        print("1. Display Profile")
        print("2. Edit Profile")
        print("3. Exit Profile Page")

        profile_choice = input("\nEnter your choice (1-3): ")
        clear_screen()
        

        if profile_choice == "1":
            display_profile()
        elif profile_choice == "2":
            editProfile(profile)  # Pass the shared profile dictionary
        elif profile_choice == "3":
            print("Exiting Profile Page...")
            from home_page import homepage
            homepage()
            break
        else:
            print("ERROR! TRY AGAIN.\n")
