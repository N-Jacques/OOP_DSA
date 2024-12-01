import keyboard  # Add this import
import getpass
import sqlite3
import time

db_path = "./database/data.db"  # Path to your database file
user_data = sqlite3.connect(db_path)  # Corrected variable usage here

def signup():
    print("=============================")
    print("---------- Sign up ----------")
    print("=============================")
    print("\n")
    print("Press 'Esc' at any time to go back to the main menu.\n")

    def esc_pressed():
        print("\nReturning to Main Menu...")
        return True

    try:
        while True:
            if keyboard.is_pressed('esc'):  # Check if 'Esc' is pressed
                esc_pressed()
                return

            while True:
                signup_fname = input("Enter your First Name: ").strip()
                if keyboard.is_pressed('esc'):
                    esc_pressed()
                    return
                if not signup_fname:  # Check if the input is blank
                    print("Error: First name cannot be blank.\n")
                else:
                    break  # Valid input

            while True:
                signup_lname = input("Enter your Last Name: ").strip()
                if keyboard.is_pressed('esc'):
                    esc_pressed()
                    return
                if not signup_lname:  # Check if the input is blank
                    print("Error: Last name cannot be blank.\n")
                else:
                    break  # Valid input

            while True:
                signup_user = input("Enter New Username: ")
                if keyboard.is_pressed('esc'):
                    esc_pressed()
                    return

                # Check if username already exists
                cursor = user_data.cursor()
                query = "SELECT * FROM User WHERE username = ?"
                cursor.execute(query, (signup_user,))
                result = cursor.fetchone()

                if result:
                    print("Error: Username already taken. Please choose a different username.\n")
                else:
                    break  # Username is available, exit loop

            signup_pass = getpass.getpass("Enter Password: ")
            if keyboard.is_pressed('esc'):
                esc_pressed()
                return

            signup_phone = input("Enter Phone number (09xxxxxxxxx): ")
            if keyboard.is_pressed('esc'):
                esc_pressed()
                return

            print("\nEnter your Address Details below: ")

            signup_street = input("Enter Street (Required): ")
            if keyboard.is_pressed('esc'):
                esc_pressed()
                return

            signup_house = input("Enter House No. (Required): ")
            if keyboard.is_pressed('esc'):
                esc_pressed()
                return

            signup_room = input("Enter Room No. (Leave empty if not applicable): ")
            if keyboard.is_pressed('esc'):
                esc_pressed()
                return

            signup_city = input("Enter City (Required): ")
            if keyboard.is_pressed('esc'):
                esc_pressed()
                return

            signup_region = input("Enter Region (Leave empty if not applicable): ")
            if keyboard.is_pressed('esc'):
                esc_pressed()
                return

            signup_zip = input("Enter Zip Code (Leave empty if not applicable): ")
            if keyboard.is_pressed('esc'):
                esc_pressed()
                return

            # Insert user details into the User table
            cursor = user_data.cursor()
            insert_user_query = """
            INSERT INTO User (first_name, last_name, username, password, phone_number) 
            VALUES (?, ?, ?, ?, ?)
            """
            cursor.execute(insert_user_query, (signup_fname, signup_lname, signup_user, signup_pass, signup_phone))
            user_data.commit()

            # Insert address into the Address table
            insert_address_query = """
            INSERT INTO Address (street_name, house_number, room_number, city, region, zip_code) 
            VALUES (?, ?, ?, ?, ?, ?)
            """
            cursor.execute(insert_address_query, (signup_street, signup_house, signup_room or None, signup_city, signup_region or None, signup_zip or None))
            user_data.commit()

            print("\nSign up successful! Please log in.")
            time.sleep(2)
            break  # Successful sign-up; exit loop

    except sqlite3.Error as e:
        print(f"Database error: {e}")

    except KeyboardInterrupt:
        print("\nReturning to main menu...")

    finally:
        if cursor:
            cursor.close()
