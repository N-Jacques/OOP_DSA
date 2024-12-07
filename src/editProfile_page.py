import time
import os
import sqlite3

# Path to the SQLite database file
db_path = "./database/data.db"

def clear_screen():
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For macOS/Linux
        os.system('clear')


def editProfile(user_profile):
    """Allows the user to edit their profile and saves changes to the database."""
    while True:
        print("\nEdit Profile Page:")
        print("1. Edit Username")
        print("2. Edit Profile Name")
        print("3. Edit Password")
        print("4. Edit Address")
        print("5. Edit Phone Number")
        print("6. Exit Edit Options")

        choice = input("\nEnter your choice (1-6): ").strip()

        try:
            # Connect to the database
            user_data = sqlite3.connect(db_path)
            cursor = user_data.cursor()

            if choice == "1":
                clear_screen()
                new_username = input("\nEnter new username: ").strip()
                cursor.execute("UPDATE user SET username = ? WHERE user_id = ?", (new_username, user_profile["user_id"]))  
                user_profile["username"] = new_username  # Update the profile dictionary
                user_data.commit()
                print("Username updated successfully!\n")
                time.sleep(0.5)
                clear_screen()

            elif choice == "2":
                clear_screen()
                new_first_name = input("\nEnter new first name: ").strip()
                new_last_name = input("\nEnter new last name: ").strip()
                cursor.execute("UPDATE user SET first_name = ?, last_name = ? WHERE user_id = ?", 
                               (new_first_name, new_last_name, user_profile["user_id"]))  
                user_profile["profile_name"] = f"{new_first_name} {new_last_name}"  
                user_data.commit()
                print("Profile name updated successfully!\n")
                time.sleep(0.5)
                clear_screen()

            elif choice == "3":
                clear_screen()
                new_password = input("\nEnter new password: ").strip()
                cursor.execute("UPDATE user SET password = ? WHERE user_id = ?", (new_password, user_profile["user_id"]))  
                user_profile["password"] = new_password  
                user_data.commit()
                print("Password updated successfully!\n")
                time.sleep(0.5)
                clear_screen()

            elif choice == "4":
                clear_screen()
                new_address = input("\nEnter new address : ").strip()
                cursor.execute("UPDATE user SET address = ? WHERE user_id = ?", (new_address, user_profile["user_id"]))  
                user_profile["address_id"] = new_address 
                user_data.commit()
                print("Address updated successfully!\n")
                time.sleep(0.5)
                clear_screen()

            elif choice == "5":
                clear_screen()
                new_phone_number = input("\nEnter new phone number: ").strip() 
                cursor.execute("UPDATE user SET phone_number = ? WHERE user_id = ?", (new_phone_number, user_profile["user_id"]))  
                user_profile["phone_number"] = new_phone_number  
                user_data.commit()
                print("Phone number updated successfully!\n")
                time.sleep(0.5)
                clear_screen()

            elif choice == "6":
                clear_screen()
                print("Exiting Edit Options...\n")
                from src.profile_page import profile_page
                break

            else:
                print("Invalid choice. Please try again.")
                time.sleep(1)
                clear_screen()

        finally:
            user_data.close()  # Ensure the connection is closed
