from profile_page import profile_page
from products_page import products


def homepage():
    print()


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
        homepage()

        print()
        print()

        print("Press Enter to return")        
        choice = input("Enter your choice (1-3): ").strip()
        print()
        if choice == "1":
            profile_page()
            input("\nPress Enter to return")

        elif choice == "2":
            products()
            input("\nPress Enter to return")

        elif choice == "3":
            print("\nThank you for shopping with us! Logging out")
            break

        else:
            print("invalid choice")



homepage()