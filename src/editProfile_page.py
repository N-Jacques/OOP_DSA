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


def editProfile(profile):
    """Allows the user to edit their profile and saves changes to the database."""
    while True:
        print("\nEdit Profile Page:")
        print("1. Edit Username")
        print("2. Edit Profile Name")
        print("3. Edit Password")
        print("4. Edit Address")
        print("5. Exit Edit Options")

        choice = input("\nEnter your choice (1-5): ").strip()

        try:
            # Connect to the database
            user_data = sqlite3.connect(db_path)
            cursor = user_data.cursor()

            if choice == "1":
                clear_screen()
                new_username = input("\nEnter new username: ").strip()
                cursor.execute("UPDATE user SET username = ? WHERE username = ?", (new_username, profile["username"]))
                profile["username"] = new_username
                user_data.commit()
                print("Username updated successfully!\n")
                time.sleep(0.5)
                clear_screen()

            elif choice == "2":
                clear_screen()
                new_first_name = input("\nEnter new first name: ").strip()
                new_last_name = input("\nEnter new last name: ").strip()
                cursor.execute("UPDATE user SET first_name = ?, last_name = ? WHERE username = ?", 
                               (new_first_name, new_last_name, profile["username"]))
                profile["profile_name"] = f"{new_first_name} {new_last_name}"
                user_data.commit()
                print("Profile name updated successfully!\n")
                time.sleep(0.5)
                clear_screen()

            elif choice == "3":
                clear_screen()
                new_password = input("\nEnter new password: ").strip()
                cursor.execute("UPDATE user SET password = ? WHERE username = ?", (new_password, profile["username"]))
                profile["password"] = new_password
                user_data.commit()
                print("Password updated successfully!\n")
                time.sleep(0.5)
                clear_screen()

            elif choice == "4":
                clear_screen()
                new_address_id = input("\nEnter new address ID: ").strip()
                cursor.execute("UPDATE user SET address_id = ? WHERE username = ?", (new_address_id, profile["username"]))
                profile["address_id"] = new_address_id
                user_data.commit()
                print("Address updated successfully!\n")
                time.sleep(0.5)
                clear_screen()

            elif choice == "5":
                clear_screen()
                print("Exiting Edit Options...\n")
                break

            else:
                print("Invalid choice. Please try again.")
                time.sleep(1)
                clear_screen()

        except sqlite3.Error as e:
            print(f"Database error: {e}")
            user_data.rollback()  # Rollback on error

        finally:
            user_data.close()  # Ensure the connection is closed

