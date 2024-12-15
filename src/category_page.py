import os
import sqlite3
from src.products_page import display_products, product_selection
from src.productDetails_page import display_product_details
from colorama import Fore, Style, init

db_path = "./database/data.db"  # Path to your SQLite database

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def category_page(user_id):
    while True:
        clear_screen()
        print(Fore.GREEN + "=" * 70)
        print(Fore.YELLOW + Style.BRIGHT +"██████╗ █████╗ ████████╗███████╗ ██████╗  ██████╗ ██████╗ ██╗   ██╗  ")
        print(Fore.YELLOW + Style.BRIGHT +"██╔════╝██╔══██╗╚══██╔══╝██╔════╝██╔════╝ ██╔═══██╗██╔══██╗╚██╗ ██╔╝ ")
        print(Fore.YELLOW + Style.BRIGHT +"██║     ███████║   ██║   █████╗  ██║  ███╗██║   ██║██████╔╝ ╚████╔╝  ")
        print(Fore.YELLOW + Style.BRIGHT +"██║     ██╔══██║   ██║   ██╔══╝  ██║   ██║██║   ██║██╔══██╗  ╚██╔╝   ") 
        print(Fore.YELLOW + Style.BRIGHT +"╚██████╗██║  ██║   ██║   ███████╗╚██████╔╝╚██████╔╝██║  ██║   ██║    ")
        print(Fore.YELLOW + Style.BRIGHT +" ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝   ╚═╝    ")
        print(Fore.GREEN + "=" * 70)

        print("1. Appliances")
        print("2. Toiletries")
        print("3. Kitchenware")
        print("4. Furnitures")
        print("5. Electronics")
        print()
        print(Fore.GREEN + "=" * 70)
        productPage_choice = input("Enter your choice (or 0 for back):  ")

        categories = {
            '1': "Appliances",
            '2': "Toiletries",
            '3': "Kitchenware",
            '4': "Furniture",
            '5': "Electronics"
        }

        if productPage_choice in categories:
            clear_screen()
            from src.products_page import products_page
            products_page(category=categories[productPage_choice], user_id=user_id)  # Pass user_id here
        elif productPage_choice == '0':
            clear_screen()
            from src.home_page import home  # Assuming home is imported here
            home(user_id)  # Pass user_id to the home function
            break
        else:
            print("Invalid Choice. Try again.")