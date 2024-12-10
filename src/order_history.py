import os
import time
import sqlite3
from colorama import Fore, Style

db_path = "./database/data.db"


def clear_screen():
    """Clears the terminal screen."""
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For macOS/Linux
        os.system('clear')


def fetch_order_history(user_id):
    """Fetch order history from the database for a given user."""
    try:
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()
        query = """SELECT o.order_date, p.product_name, o.quantity, o.status FROM orders 
        JOIN products p ON o.product_id = p.product_id WHERE o.user_id = ? ORDER BY o.order_date DESC"""
        cursor.execute(query, (user_id,))
        orders = cursor.fetchall()
        connection.close()
        return orders
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []


def order_history(order_list):
    """Display the order history table."""
    if not order_list:
        print("\nNo orders found.")
        return

    print("-" * 57)
    print(f"{'Date':<12} {'Item Name':<20} {'Quantity':<8} {'Status':<12}")
    print("-" * 57)
    for order in order_list:
        date, item_name, quantity, status = order
        print(f"{date:<12} {item_name:<20} {quantity:<8} {status:<12}")
    print("-" * 57)


def order_choice(user_id):
    """Display order choices to the user."""
    while True:
        clear_screen()

        # Fetch and display order history
        orders = fetch_order_history(user_id)
        order_history(orders)

        print("\n1. Refresh Order History")
        print("2. Exit Order History")
        print("3. Log Out")

        choice = input("\nEnter your choice (1-3): ").strip()

        if choice == "1":
            continue
        elif choice == "2":
            print("\nExiting Order History...")
            time.sleep(1)
            break
        elif choice == "3":
            from src.startup_page import startup
            print("\nLogging out...")
            time.sleep(1)
            startup()
        else:
            print("Invalid choice! Please try again.")
            time.sleep(1)
