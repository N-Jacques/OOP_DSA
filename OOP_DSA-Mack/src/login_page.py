# import keyboard

def login():
    print("\n\n---------- Login Page ----------")
    print("\n")
    print("Type 'Esc' at any time to go back to the main menu.\n\n")

    try:
        while True:
            # Check if "Esc" key is pressed
            '''
            if keyboard.is_pressed('esc'):
                print("\nReturning to main menu...")
                
                return  # Exit the login function and return to `startup() '''

            login_user = input("Enter username: ")
            if login_user.lower() == 'esc':
                print("Returning to Main Menu...")
                return
           

            login_pass = input("Enter password: ")
            if login_pass.lower() == 'esc':
                print("Returning to Main Menu...")
                return

            print("Login successful, moving to Home...")
            print(f"Welcome back, {login_user}!")
            

            break  # Successful login; exit loop
    
    except KeyboardInterrupt:
        print("\nReturning to main menu...")
        return  
    
