import os
import time
import sqlite3
import sys

# Clears the terminal screen.
def clear_screen():
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For macOS/Linux
        os.system('clear')

def order_history():  # Display header

    print("-" * 57)
    print(f"{'Date':<12} {'Item name':<20} {'Quantity':<8} {'Status':<12}")
    print("-" * 57)

    
    orders = [ # Sample order data
        ("10/24/2023", "2 TB HDD KINGSTON", 1, "Delivered"),
        ("07/30/2024", "Intel I5 7th Gen", 1, "Delivered"),
        ("04/06/2024", "DDR4 16GB RAM 1333mhz", 2, "Delivered"),
        ("08/30/2024", "500 GB SSD KINGSTON", 1, "Delivered"),
    ]
    
    for order in orders:
        date, item_name, quantity, status = order
        print(f"{date:<12} {item_name:<20} {quantity:<8} {status:<12}")
    print("-" * 57)

def order_choice(user_id): 
    while True:
        clear_screen()
        order_history()
        print("1. Exit Order History")
        print("2. Log Out")

        user_choice = input("\nEnter your choice (1-2): ").strip()

        if user_choice == "1":
            from src.profile_page import profile_page  
            profile_page(user_id)  

        elif user_choice == "2":
            print("Logging out...")
            time.sleep(0.5)
            sys.exit()

        else:
            print("Invalid choice! Please try again.\n")
            time.sleep(1)

