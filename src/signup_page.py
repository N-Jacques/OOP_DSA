#import keyboard

def signup():
    print("=============================")
    print("---------- Sign up ----------")
    print("=============================")
    print("\n")
    print("Type 'Esc' at any time to go back to the main menu.\n")

    try:
        while True:
            # Check if "Esc" key is pressed
            '''
            if keyboard.is_pressed('esc'):
                print("\nReturning to main menu...")
                
                return  # Exit the login function and return to `startup() '''

            signup_name = input("Enter your Name: ")
            if signup_name.lower() == 'esc':
                print("Returning to Main Menu...")
                return

            signup_user = input("Enter New Username: ")
            if signup_user.lower() == 'esc':
                print("Returning to Main Menu...")
                return
           

            signup_pass = input("Enter Password: ")
            if signup_pass.lower() == 'esc':
                print("Returning to Main Menu...")
                return

            print("Sign up successful, Please Log in")
            
            break  # Successful login; exit loop
    
    except KeyboardInterrupt:
        print("\nReturning to main menu...")
        return

