#import keyboard
import getpass
from src.home_page import homepage

def login():
    print("===========================")
    print("---------- Login ----------")
    print("===========================")
    print("\n")
    print("Type 'Esc' at any time to go back to the main menu.\n")

    try:
        while True:
            # Check if "Esc" key is pressed
            
            '''if keyboard.is_pressed("esc"):
                print("\nReturning to main menu...")
                from startup_page import startup
                startup()
                
                return  # Exit the login function and return to startup() '''

            login_user = input("Enter username: ")
            if login_user.lower() == 'esc':
                print("Returning to Main Menu...")
                return
            
            # getpass for password hiding when input 
            login_pass = getpass.getpass("Enter password: ")
            if login_pass.lower() == 'esc':
                print("Returning to Main Menu...")
                return

            print("Login successful, moving to Home...")
            print(f"Welcome back, {login_user}!")
            
            homepage()
            break  # Successful login; exit loop

            
    
    except KeyboardInterrupt:
        print("\nReturning to main menu...")
        return  
    

