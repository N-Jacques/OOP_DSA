from login_page import login
from signup_page import signup
from home_page import homepage
from colorama import Fore, Back, Style, init
import sys
import time 
import getpass
import os


init(autoreset=True) # Initialize Colorama 

def clear_screen(): # Clear screen every input 
    os.system('cls' if os.name == 'nt' else 'clear')

def startup(): # 
    while True:  # Allow the user to return here
        try:
            clear_screen()

            print(Fore.GREEN + "="* 65)
            print()
            print(Fore.YELLOW + Style.BRIGHT + "██╗  ██╗ ██████╗ ██╗      █████╗ ██████╗ ███████╗██╗     ███████╗")
            print(Fore.YELLOW + Style.BRIGHT + "██║  ██║██╔═══██╗██║     ██╔══██╗██╔══██╗██╔════╝██║     ██╔════╝")
            print(Fore.YELLOW + Style.BRIGHT + "███████║██║   ██║██║     ███████║██████╔╝█████╗  ██║     ███████╗")
            print(Fore.YELLOW + Style.BRIGHT + "██╔══██║██║   ██║██║     ██╔══██║██╔══██╗██╔══╝  ██║     ╚════██║")
            print(Fore.YELLOW + Style.BRIGHT + "██║  ██║╚██████╔╝███████╗██║  ██║██████╔╝███████╗███████╗███████║")
            print(Fore.YELLOW + Style.BRIGHT + "╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═════╝ ╚══════╝╚══════╝╚══════╝")
            print()
            print(Fore.WHITE + Style.BRIGHT + "\t\t\t   SHOPPING" + Style.RESET_ALL)
            print(Fore.GREEN + "=" * 65 + "\n")
            print(Fore.WHITE + "To browse our products, Login or Sign up to get started.\n")



            print(Style.BRIGHT + "\t[1] Login")
            print(Style.BRIGHT + "\t[2] Sign Up")
            print(Style.BRIGHT + "\t[3] Exit")
            print("\n")

            login1 = int(input("Enter choice (1/2/3): "))

            if login1 == 1:  # Login Page
                clear_screen()
                login()
                time.sleep(3)
                clear_screen()
                homepage()
                

            elif login1 == 2:  # Sign-up Page
                clear_screen()
                signup()

            elif login1 == 3:  # Exit
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

                
                
                # sys.exit()
        
            else:
                print("Invalid choice. Please select a valid option.")
                

        except ValueError:
            print("Invalid input. Please enter a number")
            

startup()