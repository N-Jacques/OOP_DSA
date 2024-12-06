from src.profile_page import profile_page
from src.category_page import category_page
from src.cart_page import view_cart
from src.order_history import order_history
import sqlite3
import os 


def clear_screen(): #clears screen
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def home(user_id): # main function of the homepage

    # Link database
    db_path = "./database/data.db"  # Correct path to the database file
    user_data = sqlite3.connect(db_path)  # Establish a new connection to the database


    # Access the database
    cursor = user_data.cursor()
    query = "SELECT first_name FROM User WHERE user_id = ?" # get first name from database

    cursor.execute(query, (user_id,))
    result = cursor.fetchone()  # Fetch the result
    
    
    while True:
        clear_screen() 

        print("=" * 40)
        print()
        print("SELECT(1-3):")
        print()
        print("1. PROFILE")
        print("2. VIEW PRODUCTS")
        print("3. VIEW CART")
        print("4. VIEW ORDER HISTORY")
        print("5. LOG OUT")
        print("=" * 40)

        print()
        print()

        print("Press Enter to return")
        choice = input("Enter your choice (1-5): ").strip()
        print()

        if choice == "1":
            clear_screen()
            profile_page(user_id) # TODO insert user_id when done linking user_id in profile page 
            input("\nPress Enter to return")

        elif choice == "2":
            clear_screen()
            category_page()
            input("\nPress Enter to return")

        elif choice == "3":
            clear_screen()
            view_cart() # TODO insert user_id when done linking user_id in cart page 
            input("\nPress Enter to return")

        elif choice == "4":
            clear_screen()
            order_history() # TODO insert user_id when done linking user_id in order history page 
            input("\nPress Enter to return")

        elif choice == "5":
            clear_screen()
            print("\nThank you for shopping with us! Logging out")
            break

        else:
            clear_screen()
            print("Invalid choice")

