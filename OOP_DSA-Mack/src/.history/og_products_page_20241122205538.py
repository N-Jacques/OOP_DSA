import os
import colorama
from colorama import Fore, Style, Back

colorama.init(autoreset=True)

CATEGORIES = [
    (Fore.RED + "Clothes" + Style.RESET_ALL),
    (Fore.GREEN + "Jewelry" + Style.RESET_ALL),
    (Fore.BLUE + "Appliances" + Style.RESET_ALL),
    (Fore.YELLOW + "Toiletries" + Style.RESET_ALL),
    (Fore.MAGENTA + "Kitchenware" + Style.RESET_ALL)
]

PRODUCTS = {
    "Clothes": [
        {"id": 1, "name": "T-Shirt", "price": 19.99},
        {"id": 2, "name": "Jeans", "price": 49.99}
    ],
    "Jewelry": [
        {"id": 1, "name": "Necklace", "price": 99.99},
        {"id": 2, "name": "Earrings", "price": 79.99}
    ],
    "Appliances": [
        {"id": 1, "name": "Blender", "price": 69.99},
        {"id": 2, "name": "Toaster", "price": 39.99}
    ],
    "Toiletries": [
        {"id": 1, "name": "Shampoo", "price": 12.99},
        {"id": 2, "name": "Soap", "price": 5.99}
    ],
    "Kitchenware": [
        {"id": 1, "name": "Plate Set", "price": 34.99},
        {"id": 2, "name": "Cooking Pot", "price": 59.99}
    ]
}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_banner():
    print(Fore.CYAN + "╔" + "═" * 40 + "╗")
    print("║       " + Fore.YELLOW + "P R O D U C T  S H O P" + Fore.CYAN + "       ║")
    print("╚" + "═" * 40 + "╝" + Style.RESET_ALL)

def display_categories():
    print("\n" + Fore.WHITE + Back.BLACK + " Select Product Category " + Style.RESET_ALL)
    for i, category in enumerate(CATEGORIES, 1):
        print(f"{Fore.CYAN}[{i}]{Style.RESET_ALL} {category}")
    print(f"{Fore.CYAN}[6]{Style.RESET_ALL} " + Fore.RED + "Exit" + Style.RESET_ALL)

def main():
    clear_screen()
    display_banner()
    
    while True:
        display_categories()
        
        try:
            choice = input(f"\n{Fore.GREEN}Enter category number: {Style.RESET_ALL}")
            
            if choice == '6':
                print(Fore.YELLOW + "\nThank you for shopping!" + Style.RESET_ALL)
                break
            
            category_index = int(choice) - 1
            
            if 0 <= category_index < len(CATEGORIES):
                clear_screen()
                display_banner()
                return CATEGORIES[category_index].split("]")[-1].strip()
            else:
                print(Fore.RED + "\n❌ Invalid category. Please try again." + Style.RESET_ALL)
        
        except ValueError:
            print(Fore.RED + "\n❌ Please enter a valid number." + Style.RESET_ALL)
    
    

if __name__ == "__main__":
    main()