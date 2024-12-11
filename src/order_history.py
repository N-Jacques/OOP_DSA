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
        query = """
        SELECT order_id, order_date, amount_paid, address, order_status
        FROM orders 
        WHERE user_id = ? 
        ORDER BY order_date DESC
        """
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




    print()
    print(Fore.YELLOW + Style.BRIGHT + " ██████╗ ██████╗ ██████╗ ███████╗██████╗     ██╗  ██╗██╗███████╗████████╗ ██████╗ ██████╗ ██╗   ██╗ ")
    print(Fore.YELLOW + Style.BRIGHT + "██╔═══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗    ██║  ██║██║██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗╚██╗ ██╔╝ ")
    print(Fore.YELLOW + Style.BRIGHT + "██║   ██║██████╔╝██║  ██║█████╗  ██████╔╝    ███████║██║███████╗   ██║   ██║   ██║██████╔╝ ╚████╔╝  ")
    print(Fore.YELLOW + Style.BRIGHT + "██║   ██║██╔══██╗██║  ██║██╔══╝  ██╔══██╗    ██╔══██║██║╚════██║   ██║   ██║   ██║██╔══██╗  ╚██╔╝   ")
    print(Fore.YELLOW + Style.BRIGHT + "╚██████╔╝██║  ██║██████╔╝███████╗██║  ██║    ██║  ██║██║███████║   ██║   ╚██████╔╝██║  ██║   ██║    ")
    print(Fore.YELLOW + Style.BRIGHT + "╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝    ╚═╝  ╚═╝╚═╝╚══════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝   ╚═╝     ")



    print(Fore.GREEN + Style.BRIGHT +"=" * 100)
    print(f"{'Order ID':<18} {'Date':<18} {'Amount':<20} {'Address':<31}{'Status':<12}")
    print(Fore.GREEN + Style.BRIGHT +"=" * 100)

    for order in order_list:
        order_id, order_date, amount_paid, address, order_status = order
        print(f"{order_id:<12} {order_date:<24} {amount_paid:<11} {address:<40}{ order_status:<20}")
    print(Fore.GREEN + Style.BRIGHT +"=" * 100)


def order_choice(user_id):
    """Display order choices to the user."""
    while True:
        clear_screen()

        # Fetch and display order history
        orders = fetch_order_history(user_id)
        order_history(orders)

        print("\n1. Refresh Order History")
    

        choice = input("\nEnter your choice. / for back: ").strip()

        if choice == "1":
            continue
        elif choice == "/":
            print("\nExiting Order History...")
            time.sleep(0.5)
            break
 
        else:
            print("Invalid choice! Please try again.")
            time.sleep(0.5)
