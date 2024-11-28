import time
from editProfile_page import edit_page


profile = {
    "username": "default_user",
    "profile_name": "Default Name",
    "password": "default_password",
    "address": "default_address"
}

def display_profile():
    print("Accessing your profile...")
    print()
    time.sleep(2)

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

        choice = input("\nEnter your choice (1-3): ")

        if choice == "1":
            display_profile()
        elif choice == "2":
            edit_page(profile)  # Pass the shared profile dictionary
        elif choice == "3":
            print("Exiting Profile Page...")
            from home_page import homepage
            homepage()
            break
        else:
            print("ERROR! TRY AGAIN.\n")
