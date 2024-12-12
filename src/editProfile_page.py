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
        print(Fore.GREEN + Style.BRIGHT +"=" * 200)
        print("")
        print(Fore.YELLOW + Style.BRIGHT + "███████╗██████╗ ██╗████████╗    ██████╗ ██████╗  ██████╗ ███████╗██╗██╗     ███████╗")
        print(Fore.YELLOW + Style.BRIGHT + "██╔════╝██╔══██╗██║╚══██╔══╝    ██╔══██╗██╔══██╗██╔═══██╗██╔════╝██║██║     ██╔════╝")
        print(Fore.YELLOW + Style.BRIGHT + "█████╗  ██║  ██║██║   ██║       ██████╔╝██████╔╝██║   ██║█████╗  ██║██║     █████╗  ")
        print(Fore.YELLOW + Style.BRIGHT + "██╔══╝  ██║  ██║██║   ██║       ██╔═══╝ ██╔══██╗██║   ██║██╔══╝  ██║██║     ██╔══╝  ")
        print(Fore.YELLOW + Style.BRIGHT + "███████╗██████╔╝██║   ██║       ██║     ██║  ██║╚██████╔╝██║     ██║███████╗███████")
        print(Fore.YELLOW + Style.BRIGHT + "╚══════╝╚═════╝ ╚═╝   ╚═╝       ╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝╚══════╝")
        print("")
        print(Fore.GREEN + Style.BRIGHT +"=" * 200)        
        print("")


        print(Fore.GREEN + Style.BRIGHT +"=" * 200)
        print("\nEdit Profile Page:")
        print(Fore.GREEN + Style.BRIGHT +"=" * 200)
        print("1. Edit Password")
        print("2. Edit Address")
        print("3. Edit Phone Number")
        print("4. Delete your Account")
        print("0. Go back")
    

        editProfile_choice = input("\nEnter your editProfile_choice (1-5): ").strip()

        try:
            # Connect to the database
            user_data = sqlite3.connect(db_path)
            cursor = user_data.cursor()




            if editProfile_choice == "1":
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

            elif editProfile_choice == "2":
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

            elif editProfile_choice == "3":
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

            elif editProfile_choice == "4":
                # Delete user logic here
                confirmation = input(
                    Fore.RED + "\nAre you sure you want to delete your account? (yes/no): ").strip().lower()
                if confirmation == "yes":
                    try:
                        cursor.execute("DELETE FROM orders WHERE user_id = ?", (user_profile["user_id"],))
                        cursor.execute("DELETE FROM cart WHERE user_id = ?", (user_profile["user_id"],))
                        cursor.execute("DELETE FROM user WHERE user_id = ?", (user_profile["user_id"],)) 

                        user_data.commit()
                        cursor.execute("UPDATE sqlite_sequence SET seq = (SELECT MAX(user_id) FROM user) WHERE name = 'user'")

                        # Step 3: Execute VACUUM to rebuild and reset the database
                        cursor.execute("VACUUM")
            
                        # Commit changes
                        user_data.commit()
                        
                        cursor.execute("INSERT INTO user (first_name, last_name, username, password) VALUES (?, ?, ?, ?)", 
                        ("New", "User", "newuser", "password"))
                        cursor.execute("SELECT last_insert_rowid()")
                        new_user_id = cursor.fetchone()[0]
                        print(f"New user_id: {new_user_id}")

                        print(Fore.RED + "\nYour account has been successfully deleted. Goodbye!")
                        time.sleep(1)

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


            elif editProfile_choice == "0":
                clear_screen()
                print("Exiting Edit Options...\n")
                time.sleep(0.5)
                from src.profile_page import profile_page
                break

            else:
                print("Invalid editProfile_choice. Please try again.")
                time.sleep(0.5)
                clear_screen()

        finally:
            user_data.close()  # Ensure the connection is closed
