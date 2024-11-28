# main.py
from src.startup_page import startup
from src.login_page import login
from src.signup_page import signup # type: ignore


def main():
    print("Welcome to Online Shopping!")
    while True:
        print("\n1. Startup\n2. Login\n3. Signup\n4. Exit")
        choice = input("Select an option: ")
        if choice == "1":
            startup()
        elif choice == "2":
            login()
        elif choice == "3":
            signup()
        elif choice == "4":
            print("Thank you for using Online Shopping!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
