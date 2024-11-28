import time


profile = {
    "username": " ",
    "profile_name": " ",
    "password": " "
}

def edit_page():
    while True:
        print("\nEdit Profile Page:")
        print("1. Edit Username")
        print("2. Edit Profile Name")
        print("3. Edit Password")
        print("4. Exit Edit Options")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            new_username = input("Enter new username: ").strip()
            profile["username"] = new_username
            print("Username updated successfully!\n")
            from profile_page import profile_page
            profile_page()  
            break
        elif choice == "2":
            new_name = input("Enter new profile name: ").strip()
            profile["profile_name"] = new_name
            print("Profile name updated successfully!\n")
            from profile_page import profile_page
            profile_page() 
            break
        elif choice == "3":
            new_password = input("Enter new password: ").strip()
            profile["password"] = new_password
            print("Password updated successfully!\n")
            from profile_page import profile_page
            profile_page()  
            break
        elif choice == "4":
            print("Exiting Edit Options...")
            profile_page()  
            break
        else:
            print("Invalid choice. Please try again.\n")


edit_page()