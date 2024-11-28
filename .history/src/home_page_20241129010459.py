from profile_page import profile_page
import os


def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def homepage():
    print()
    print("=" * 40)
    print()
    print("SELECT(1-3):")
    print()
    print("1. PROFILE")
    print("2. VIEW PRODUCTS")
    print("3. LOG OUT")
    print("=" * 40)

    while True:
        clear_screen()

        print()
        print()

        print("Press Enter to return")
        choice = input("Enter your choice (1-3): ").strip()
        print()
        
        if choice == "1":
            clear_screen()
            profile_page()
            input("\nPress Enter to return")

        elif choice == "2":
            clear_screen()
            #dito nakalagay view catego
            input("\nPress Enter to return")

        elif choice == "3":
            clear_screen()
            print("\nThank you for shopping with us! Logging out")
            break

        else:
            clear_screen()
            print("Invalid choice")




