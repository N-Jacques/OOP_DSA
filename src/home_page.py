# In home_page.py
from src.profile_page import profile_page
from src.category_page import category_page
from src.cart_page import view_cart
import os

<<<<<<< Updated upstream

def clear_screen():
=======
def clear_screen():  # Clears screen
>>>>>>> Stashed changes
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# home_page.py

<<<<<<< Updated upstream
def homepage():
=======
def home(username):  # Accept `username` as a parameter
>>>>>>> Stashed changes
    while True:
        clear_screen()  # Clears the screen before showing the menu
        print("=" * 40)
        print()
        print("SELECT(1-5):")
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
            profile_page(username)  # Pass `username` to `profile_page()`
            input("\nPress Enter to return")

        elif choice == "2":
            clear_screen()
            category_page()
            input("\nPress Enter to return")

        elif choice == "3":
            clear_screen()
            view_cart()
            input("\nPress Enter to return")

        elif choice == "4":
            clear_screen()
            category_page()
            input("\nPress Enter to return")

        elif choice == "5":
            clear_screen()
            print("\nThank you for shopping with us! Logging out")
            break

        else:
            clear_screen()
            print("Invalid choice")
