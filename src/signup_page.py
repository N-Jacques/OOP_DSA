import getpass
import sqlite3
import time

db_path = "./database/data.db"  # Path to your database file
user_data = sqlite3.connect('db_path')  # Connect to the database

def signup():
    print("=============================")
    print("---------- Sign up ----------")
    print("=============================")
    print("\n")
    print("Type 'Esc' at any time to go back to the main menu.\n")

    try:
        while True:
            signup_fname = input("Enter your First Name: ")
            if signup_fname.lower() == 'esc':
                print("Returning to Main Menu...")
                return
            
            signup_lname = input("Enter your Last Name: ")
            if signup_lname.lower() == 'esc':
                print("Returning to Main Menu...")
                return

            signup_user = input("Enter New Username: ")
            if signup_user.lower() == 'esc':
                print("Returning to Main Menu...")
                return
           
            signup_pass = getpass.getpass("Enter Password: ")
            if signup_pass.lower() == 'esc':
                print("Returning to Main Menu...")
                return
            
            signup_phone = input("Enter Phone number (09xxxxxxxxx): ")
            if signup_phone.lower() == 'esc':
                print("Returning to Main Menu...")
                return
            
            print("\nEnter your Address Details below: ")
            
            signup_street = input("Enter Street (Required): ")
            if signup_street.lower() == 'esc':
                print("Returning to Main Menu...")
                return

            signup_house = input("Enter House No. (Required): ")
            if signup_house.lower() == 'esc':
                print("Returning to Main Menu...")
                return
            
            signup_room = input("Enter Room No. (Leave empty if not applicable): ")
            if signup_room.lower() == 'esc':
                print("Returning to Main Menu...")
                return
            
            signup_city = input("Enter City (Required): ")
            if signup_city.lower() == 'esc':
                print("Returning to Main Menu...")
                return
            
            signup_region = input("Enter Region (Leave empty if not applicable): ")
            if signup_region.lower() == 'esc':
                print("Returning to Main Menu...")
                return
            
            signup_zip = input("Enter Zip Code (Leave empty if not applicable): ")
            if signup_zip.lower() == 'esc':
                print("Returning to Main Menu...")
                return

            # Check if the username already exists
            cursor = user_data.cursor()
            query = "SELECT * FROM User WHERE username = ?"
            cursor.execute(query, (signup_user,))
            result = cursor.fetchone()

            if result:
                print("Username already exists. Please choose a different one.")
            else:
                # Insert user details into the User table
                insert_user_query = "INSERT INTO User (first_name, last_name, username, password, phone_number) VALUES (?, ?, ?, ?, ?)"
                cursor.execute(insert_user_query, (signup_fname, signup_lname, signup_user, signup_pass, signup_phone))
                user_data.commit()

                # Get the last inserted user_id (if User and Address are linked)
                user_id = cursor.lastrowid
                
                # Insert address details into the Address table
                insert_address_query = """INSERT INTO Address (street_name, house_number, room_number, city, region, zip_code) 
                                          VALUES (?, ?, ?, ?, ?, ?)"""
                cursor.execute(insert_address_query, (signup_street, signup_house, signup_room, signup_city, signup_region, signup_zip))
                user_data.commit()

                print("\nSign up successful! Please log in.")
                time.sleep(2)
                break  # Successful sign-up; exit loop
    
    except KeyboardInterrupt:
        print("\nReturning to main menu...")
        return
    finally:
        user_data.close()  # Ensure the database connection is closed
