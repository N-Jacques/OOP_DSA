import time
from edit_page import edit_page
import os

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
    time.sleep(0.5)

    print("=" * 40)
    print(f"Username: {profile['username']}")
    print(f"Name: {profile['profile_name']}")
    print(f"Password: {profile['password']}")
    print(f"Address: {profile['address']}")

    print(f"Order History: 5 orders")
    print("=" * 40)

def profile_page():
    while True:
        print("\nProfile Page:")
       
        print()
        display_profile()
        print()
    
        print("1. Edit Profile")
        print("2. Exit Profile Page")

        choice = input("\nEnter your choice (1-2): ")
        clear_screen()

        if choice == "1":
            clear_screen()
            edit_page(profile)             

        elif choice == "2":
            print("Exiting Profile Page...")
            from home_page import homepage
            homepage() 
            break


        else:
            print("ERROR! TRY AGAIN.\n")


clear_screen()  
