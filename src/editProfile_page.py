import time
import os
import sqlite3
import sys
from colorama import Fore, Style, init

# Path to the SQLite database file
db_path = "./database/data.db"

def clear_screen():
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For macOS/Linux
        os.system('clear')

def delete_user(cursor, user_id, connection):
    """Delete the user and all related data from the database."""
    try:
        confirmation = input(
            Fore.RED + "\nAre you sure you want to delete your account? (yes/no): ").strip().lower()
        if confirmation == "yes":
            
            cursor.execute("DELETE FROM orders WHERE user_id = ?", (user_id,))
            cursor.execute("DELETE FROM cart WHERE user_id = ?", (user_id,))
            cursor.execute("DELETE FROM address WHERE address IN (SELECT address FROM user WHERE user_id = ?)", (user_id,))
            cursor.execute("DELETE FROM user WHERE user_id = ?", (user_id,))

            # confirm
            connection.commit()
            print(Fore.RED + "\nYour account has been successfully deleted. Goodbye!")
            time.sleep(2)

            
            from src.startup_page import startup
            startup()
        else:
            print(Fore.YELLOW + "\nAccount deletion canceled.")
            time.sleep(1)
    except sqlite3.Error as e:
        print(Fore.RED + f"\nDatabase error: {e}")
        connection.rollback()
    finally:
        clear_screen()


def editProfile(user_profile):
    """Allows the user to edit their profile and saves changes to the database."""
    while True:
        # header of home
        print(Fore.GREEN + "=" * 49)
        print("")
        print(Fore.YELLOW + Style.BRIGHT + "███████╗██████╗ ██╗████████╗    ██████╗ ██████╗  ██████╗ ███████╗██╗██╗     ███████╗")
        print(Fore.YELLOW + Style.BRIGHT + "██╔════╝██╔══██╗██║╚══██╔══╝    ██╔══██╗██╔══██╗██╔═══██╗██╔════╝██║██║     ██╔════╝")
        print(Fore.YELLOW + Style.BRIGHT + "█████╗  ██║  ██║██║   ██║       ██████╔╝██████╔╝██║   ██║█████╗  ██║██║     █████╗  ")
        print(Fore.YELLOW + Style.BRIGHT + "██╔══╝  ██║  ██║██║   ██║       ██╔═══╝ ██╔══██╗██║   ██║██╔══╝  ██║██║     ██╔══╝  ")
        print(Fore.YELLOW + Style.BRIGHT + "███████╗██████╔╝██║   ██║       ██║     ██║  ██║╚██████╔╝██║     ██║███████╗███████")
        print(Fore.YELLOW + Style.BRIGHT + "╚══════╝╚═════╝ ╚═╝   ╚═╝       ╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝╚══════╝")
        print("")
        print(Fore.GREEN + "=" * 49)
        print("")

        print("\nEdit Profile Page:")
        print("1. Edit Username")
        print("2. Edit Profile Name")
        print("3. Edit Password")
        print("4. Edit Address")
        print("5. Edit Phone Number")
        print("6. Delete your Account")
        print("7. Exit Edit Options")
        print("8. Log out")

        choice = input("\nEnter your choice (1-6): ").strip()

        try:
            # Connect to the database
            user_data = sqlite3.connect(db_path)
            cursor = user_data.cursor()

            if choice == "1":
                clear_screen()
                
                # header of home
                print(Fore.GREEN + "=" * 49)
                print("")
                print(Fore.YELLOW + Style.BRIGHT + "███████╗██████╗ ██╗████████╗    ██╗   ██╗███████╗███████╗██████╗ ███╗   ██╗ █████╗ ███╗   ███╗███████")
                print(Fore.YELLOW + Style.BRIGHT + "██╔════╝██╔══██╗██║╚══██╔══╝    ██║   ██║██╔════╝██╔════╝██╔══██╗████╗  ██║██╔══██╗████╗ ████║██╔════╝")
                print(Fore.YELLOW + Style.BRIGHT + "█████╗  ██║  ██║██║   ██║       ██║   ██║███████╗█████╗  ██████╔╝██╔██╗ ██║███████║██╔████╔██║█████╗  ")
                print(Fore.YELLOW + Style.BRIGHT + "██╔══╝  ██║  ██║██║   ██║       ██║   ██║╚════██║██╔══╝  ██╔══██╗██║╚██╗██║██╔══██║██║╚██╔╝██║██╔══╝  ")
                print(Fore.YELLOW + Style.BRIGHT + "███████╗██████╔╝██║   ██║       ╚██████╔╝███████║███████╗██║  ██║██║ ╚████║██║  ██║██║ ╚═╝ ██║███████╗")
                print(Fore.YELLOW + Style.BRIGHT + "╚══════╝╚═════╝ ╚═╝   ╚═╝        ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝")
                print("")
                print(Fore.GREEN + "=" * 49)
                print("")


                new_username = input("\nEnter new username: ").strip()
                cursor.execute("UPDATE user SET username = ? WHERE user_id = ?", (new_username, user_profile["user_id"]))  
                user_profile["username"] = new_username  # Update the profile dictionary
                user_data.commit()
                print("Username updated successfully!\n")
                time.sleep(0.5)
                clear_screen()

            elif choice == "2":
                clear_screen()

                # header of edit name
                print(Fore.GREEN + "=" * 49)
                print("")
                print(Fore.YELLOW + Style.BRIGHT + "███████╗██████╗ ██╗████████╗    ███╗   ██╗ █████╗ ███╗   ███╗███████")
                print(Fore.YELLOW + Style.BRIGHT + "██╔════╝██╔══██╗██║╚══██╔══╝    ████╗  ██║██╔══██╗████╗ ████║██╔════╝")
                print(Fore.YELLOW + Style.BRIGHT + "█████╗  ██║  ██║██║   ██║       ██╔██╗ ██║███████║██╔████╔██║█████╗  ")
                print(Fore.YELLOW + Style.BRIGHT + "██╔══╝  ██║  ██║██║   ██║       ██║╚██╗██║██╔══██║██║╚██╔╝██║██╔══╝  ")
                print(Fore.YELLOW + Style.BRIGHT + "███████╗██████╔╝██║   ██║       ██║ ╚████║██║  ██║██║ ╚═╝ ██║███████╗")
                print(Fore.YELLOW + Style.BRIGHT + "╚══════╝╚═════╝ ╚═╝   ╚═╝       ╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝")
                print("")
                print(Fore.GREEN + "=" * 49)
                print("")

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

                # banner for edit password
                print(Fore.GREEN + "=" * 100)
                print("")
                print(Fore.YELLOW + Style.BRIGHT + "███████╗██████╗ ██╗████████╗    ██████╗  █████╗ ███████╗███████╗██╗    ██╗ ██████╗ ██████╗ ██████╗ ")
                print(Fore.YELLOW + Style.BRIGHT + "██╔════╝██╔══██╗██║╚══██╔══╝    ██╔══██╗██╔══██╗██╔════╝██╔════╝██║    ██║██╔═══██╗██╔══██╗██╔══██╗")
                print(Fore.YELLOW + Style.BRIGHT + "█████╗  ██║  ██║██║   ██║       ██████╔╝███████║███████╗███████╗██║ █╗ ██║██║   ██║██████╔╝██║  ██║")                    
                print(Fore.YELLOW + Style.BRIGHT + "██╔══╝  ██║  ██║██║   ██║       ██╔═══╝ ██╔══██║╚════██║╚════██║██║███╗██║██║   ██║██╔══██╗██║  ██║")
                print(Fore.YELLOW + Style.BRIGHT + "███████╗██████╔╝██║   ██║       ██║     ██║  ██║███████║███████║╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝")
                print(Fore.YELLOW + Style.BRIGHT + "╚══════╝╚═════╝ ╚═╝   ╚═╝       ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝ ")
                print("")
                print(Fore.GREEN + "=" * 100)
                print("")
                print(Fore.YELLOW + Style.BRIGHT + "Type '/' at any time to go back to the main menu.\n")

                new_password = input("\nEnter new password: ").strip()
                cursor.execute("UPDATE user SET password = ? WHERE user_id = ?", (new_password, user_profile["user_id"]))  
                user_profile["password"] = new_password  
                user_data.commit()
                print("Password updated successfully!\n")
                time.sleep(0.5)
                clear_screen()

            elif choice == "4":
                clear_screen()
                
                # banner for edit address
                print(Fore.GREEN + "=" * 100)
                print("")
                print(Fore.YELLOW + Style.BRIGHT + "███████╗██████╗ ██╗████████╗     █████╗ ██████╗ ██████╗ ██████╗ ███████╗███████╗███████╗")
                print(Fore.YELLOW + Style.BRIGHT + "██╔════╝██╔══██╗██║╚══██╔══╝    ██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝")
                print(Fore.YELLOW + Style.BRIGHT + "█████╗  ██║  ██║██║   ██║       ███████║██║  ██║██║  ██║██████╔╝█████╗  ███████╗███████╗")
                print(Fore.YELLOW + Style.BRIGHT + "██╔══╝  ██║  ██║██║   ██║       ██╔══██║██║  ██║██║  ██║██╔══██╗██╔══╝  ╚════██║╚════██║")
                print(Fore.YELLOW + Style.BRIGHT + "███████╗██████╔╝██║   ██║       ██║  ██║██████╔╝██████╔╝██║  ██║███████╗███████║███████║")
                print(Fore.YELLOW + Style.BRIGHT + "╚══════╝╚═════╝ ╚═╝   ╚═╝       ╚═╝  ╚═╝╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝")
                print("")
                print(Fore.GREEN + "=" * 100)
                print("")
                print(Fore.YELLOW + Style.BRIGHT + "Type '/' at any time to go back to the main menu.\n")

                new_address = input("\nEnter new address : ").strip()
                cursor.execute("UPDATE user SET address = ? WHERE user_id = ?", (new_address, user_profile["user_id"]))  
                user_profile["address_id"] = new_address 
                user_data.commit()
                print("Address updated successfully!\n")
                time.sleep(0.5)
                clear_screen()

            elif choice == "5":
                clear_screen()
                
                # banner for edit phone number
                print(Fore.GREEN + "=" * 200)
                print("")
                print(Fore.YELLOW + Style.BRIGHT + "███████╗██████╗ ██╗████████╗    ██████╗ ██╗  ██╗ ██████╗ ███╗   ██╗███████╗    ███╗   ██╗██╗   ██╗███╗   ███╗██████╗ ███████╗██████╗ ")
                print(Fore.YELLOW + Style.BRIGHT + "██╔════╝██╔══██╗██║╚══██╔══╝    ██╔══██╗██║  ██║██╔═══██╗████╗  ██║██╔════╝    ████╗  ██║██║   ██║████╗ ████║██╔══██╗██╔════╝██╔══██╗")
                print(Fore.YELLOW + Style.BRIGHT + "█████╗  ██║  ██║██║   ██║       ██████╔╝███████║██║   ██║██╔██╗ ██║█████╗      ██╔██╗ ██║██║   ██║██╔████╔██║██████╔╝█████╗  ██████╔╝")
                print(Fore.YELLOW + Style.BRIGHT + "██╔══╝  ██║  ██║██║   ██║       ██╔═══╝ ██╔══██║██║   ██║██║╚██╗██║██╔══╝      ██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗")
                print(Fore.YELLOW + Style.BRIGHT + "███████╗██████╔╝██║   ██║       ██║     ██║  ██║╚██████╔╝██║ ╚████║███████╗    ██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██████╔╝███████╗██║  ██║")
                print(Fore.YELLOW + Style.BRIGHT + "╚══════╝╚═════╝ ╚═╝   ╚═╝       ╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝    ╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝")
                print("")
                print(Fore.GREEN + "=" * 200)

                new_phone_number = input("\nEnter new phone number: ").strip() 
                cursor.execute("UPDATE user SET phone_number = ? WHERE user_id = ?", (new_phone_number, user_profile["user_id"]))  
                user_profile["phone_number"] = new_phone_number  
                user_data.commit()
                print("Phone number updated successfully!\n")
                time.sleep(0.5)
                clear_screen()

            elif choice == "6":
                # Delete user logic here
                confirmation = input(
                    Fore.RED + "\nAre you sure you want to delete your account? (yes/no): ").strip().lower()
                if confirmation == "yes":
                    try:
                        cursor.execute("DELETE FROM orders WHERE user_id = ?", (user_profile["user_id"],))
                        cursor.execute("DELETE FROM cart WHERE user_id = ?", (user_profile["user_id"],))
                        cursor.execute("DELETE FROM user WHERE user_id = ?", (user_profile["user_id"],))
                        user_data.commit()

                        print(Fore.RED + "\nYour account has been successfully deleted. Goodbye!")
                        time.sleep(2)

                        # Redirect to startup page after deletion
                        from src.startup_page import startup
                        startup()
                        break  # Exit the loop after redirecting
                    except sqlite3.Error as e:
                        print(Fore.RED + f"\nDatabase error: {e}")
                        user_data.rollback()
                else:
                    print(Fore.YELLOW + "\nAccount deletion canceled.")
                    time.sleep(1)


            elif choice == "7":
                clear_screen()
                print("Exiting Edit Options...\n")
                from src.profile_page import profile_page
                break

            elif choice =="8":
                from src.startup_page import startup
                clear_screen()
                print("\nThank you for shopping with us! Logging out")
                time.sleep(1)
                startup()

            else:
                print("Invalid choice. Please try again.")
                time.sleep(1)
                clear_screen()

        finally:
            user_data.close()  # Ensure the connection is closed
