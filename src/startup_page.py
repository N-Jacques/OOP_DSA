from src.login_page import login
from src.signup_page import signup
from colorama import Fore, Back, Style, init
import sys
import time 
import os


init(autoreset=True) # Initialize Colorama 

def clear_screen(): # Clear screen every input 
    os.system('cls' if os.name == 'nt' else 'clear')


def startup(): # 
    while True:  # Allow the user to return here
        try:
            clear_screen()

            print(Fore.GREEN + "="* 90)
            print()
            print(Fore.YELLOW + Style.BRIGHT + "██████╗ ███████╗███████╗████████╗    ███████╗██████╗ ██╗███████╗███╗   ██╗██████╗ ███████╗")
            print(Fore.YELLOW + Style.BRIGHT + "██╔══██╗██╔════╝██╔════╝╚══██╔══╝    ██╔════╝██╔══██╗██║██╔════╝████╗  ██║██╔══██╗██╔════╝")
            print(Fore.YELLOW + Style.BRIGHT + "██████╔╝█████╗  ███████╗   ██║       █████╗  ██████╔╝██║█████╗  ██╔██╗ ██║██║  ██║███████╗")
            print(Fore.YELLOW + Style.BRIGHT + "██╔══██╗██╔══╝  ╚════██║   ██║       ██╔══╝  ██╔══██╗██║██╔══╝  ██║╚██╗██║██║  ██║╚════██║")
            print(Fore.YELLOW + Style.BRIGHT + "██████╔╝███████╗███████║   ██║       ██║     ██║  ██║██║███████╗██║ ╚████║██████╔╝███████║")
            print(Fore.YELLOW + Style.BRIGHT + "╚═════╝ ╚══════╝╚══════╝   ╚═╝       ╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═══╝╚═════╝ ╚══════╝")

            print()
            print(Fore.WHITE + Style.BRIGHT + "\t\t\t\t\tSHOPPING" + Style.RESET_ALL)
            print(Fore.GREEN + "=" * 90 + "\n")
            print(Fore.WHITE + "To browse our products, Login or Sign up to get started.\n")



            print(Style.BRIGHT + "\t[1] Login")
            print(Style.BRIGHT + "\t[2] Sign Up")
            print(Style.BRIGHT + "\t[3] Exit")
            print("\n")

            startup_choice = int(input("Enter choice (1/2/3): "))

            if startup_choice == 1:  # Login Page
                clear_screen()
                login()
                clear_screen()
                
            elif startup_choice == 2:  # Sign-up Page
                clear_screen()
                signup()

            elif startup_choice == 3:  # Exit
                clear_screen()
                print("\t\t\tExiting the program.")
                print(Fore.CYAN + "=" * 77)
                print()
                print(Fore.YELLOW + Style.BRIGHT + "████████╗██╗  ██╗ █████╗ ███╗   ██╗██╗  ██╗    ██╗   ██╗ ██████╗ ██╗   ██╗██╗")
                print(Fore.YELLOW + Style.BRIGHT + "╚══██╔══╝██║  ██║██╔══██╗████╗  ██║██║ ██╔╝    ╚██╗ ██╔╝██╔═══██╗██║   ██║██║")
                print(Fore.YELLOW + Style.BRIGHT + "   ██║   ███████║███████║██╔██╗ ██║█████╔╝      ╚████╔╝ ██║   ██║██║   ██║██║")
                print(Fore.YELLOW + Style.BRIGHT + "   ██║   ██╔══██║██╔══██║██║╚██╗██║██╔═██╗       ╚██╔╝  ██║   ██║██║   ██║╚═╝")
                print(Fore.YELLOW + Style.BRIGHT + "   ██║   ██║  ██║██║  ██║██║ ╚████║██║  ██╗       ██║   ╚██████╔╝╚██████╔╝██╗")
                print(Fore.YELLOW + Style.BRIGHT + "   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝       ╚═╝    ╚═════╝  ╚═════╝ ╚═╝")
                print()
                print(Fore.CYAN + "=" * 77 + "\n")
                time.sleep(3)
                
                sys.exit()
        
            else:
                print(Fore.RED + Style.BRIGHT +"Invalid choice. Please select a valid option.")
                time.sleep(0.5)
                

        except ValueError:
            print(Fore.RED + Style.BRIGHT +"Invalid input. Please enter a number")
            time.sleep(0.5)
            

