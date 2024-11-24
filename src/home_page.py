from category_page import category_page
from profile_page import profile_page

def home():
    print()

    

    print()
    print("=" * 40)

    print()
    print("SELECT(1-3):")
    print()\

    print("1. PROFILE")
    print("2. MAIN PAGE")
    print("3. LOG OUT")
    print("=" * 40)


def main():
    while True:
        home()

        print()
        print()

        print("Press Enter to return")        
        choice = input("Enter your choice (1-3): ").strip()
        print()
        if choice == "1":
            profile_page()
            input("\nPress Enter to return")

        elif choice == "2":
            category_page()
            input("\nPress Enter to return")

        elif choice == "3":
            print("\nThank you for shopping with us! Logging out")
            break

        else:
            print("invalid choice")


if __name__ == "__main__":
    main()
