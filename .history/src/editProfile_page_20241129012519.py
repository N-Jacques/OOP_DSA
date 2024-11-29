import time
import os


def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def edit_page(profile):
    while True:
        print("\nEdit Profile Page:")
        print("1. Edit Username")
        print("2. Edit Profile Name")
        print("3. Edit Password")
        print("4. Edit Address")
        print("5. Exit Edit Options")

        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == "1":
            clear_screen()
            new_username = input("\nEnter new username: ").strip()
            profile["username"] = new_username
            print("Username updated successfully!\n")
            time.sleep(0.5)
            clear_screen()

        elif choice == "2":
            clear_screen()
            new_name = input("\nEnter new profile name: ").strip()
            profile["profile_name"] = new_name
            print("Profile name updated successfully!\n")
            time.sleep(0.5)
            clear_screen()

        elif choice == "3":
            clear_screen()
            new_password = input("\nEnter new password: ").strip()
            profile["password"] = new_password
            print("Password updated successfully!\n")
            time.sleep(0.5)
            clear_screen()

        elif choice == "4":
            clear_screen()
            new_address = input("\nEnter new address: ").strip()
            profile["address"] = new_address
            print("Address updated successfully!\n")
            time.sleep(0.5)
            clear_screen()

        elif choice == "5":
            clear_screen()
            print("Exiting Edit Options...\n")
            from profile_page import profile_page
            profile_page()
            break

        else:
            clear_screen()
            print("Invalid choice. Please try again.")
            time.sleep(1)


clear_screen()