import os
import colorama
from colorama import Fore, Style, Back

# Initialize colorama for styled text
colorama.init(autoreset=True)

# Define categories and products
CATEGORIES = [
    {"name": "Clothes", "display": Fore.RED + "Clothes" + Style.RESET_ALL},
    {"name": "Jewelry", "display": Fore.GREEN + "Jewelry" + Style.RESET_ALL},
    {"name": "Appliances", "display": Fore.BLUE + "Appliances" + Style.RESET_ALL},
    {"name": "Toiletries", "display": Fore.YELLOW + "Toiletries" + Style.RESET_ALL},
    {"name": "Kitchenware", "display": Fore.MAGENTA + "Kitchenware" + Style.RESET_ALL},
]

PRODUCTS = {
    "Clothes": [
        {"id": 1, "name": "T-Shirt", "price": 19.99},
        {"id": 2, "name": "Jeans", "price": 49.99},
    ],
    "Jewelry": [
        {"id": 1, "name": "Necklace", "price": 99.99},
        {"id": 2, "name": "Earrings", "price": 79.99},
    ],
    "Appliances": [
        {"id": 1, "name": "Blender", "price": 69.99},
        {"id": 2, "name": "Toaster", "price": 39.99},
    ],
    "Toiletries": [
        {"id": 1, "name": "Shampoo", "price": 12.99},
        {"id": 2, "name": "Soap", "price": 5.99},
    ],
    "Kitchenware": [
        {"id": 1, "name": "Plate Set", "price": 34.99},
        {"id": 2, "name": "Cooking Pot", "price": 59.99},
    ],
}

# Utility to clear the screen
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# Display the banner
def display_banner():
    print(Fore.CYAN + "╔" + "═" * 40 + "╗")
    print("║       " + Fore.YELLOW + "P R O D U C T  S H O P" + Fore.CYAN + "       ║")
    print("╚" + "═" * 40 + "╝" + Style.RESET_ALL)

# Display categories
def display_categories():
    print("\n" + Fore.WHITE + Back.BLACK + " Select Product Category " + Style.RESET_ALL)
    for i, category in enumerate(CATEGORIES, 1):
        print(f"{Fore.CYAN}[{i}]{Style.RESET_ALL} {category['display']}")
    print(f"{Fore.CYAN}[6]{Style.RESET_ALL} " + Fore.RED + "Exit" + Style.RESET_ALL)

# Main function to handle category selection
def main():
    clear_screen()
    display_banner()
    
    while True:
        display_categories()
        try:
            choice = input(f"\n{Fore.GREEN}Enter category number: {Style.RESET_ALL}")
            if choice == "6":  # Exit option
                print(Fore.YELLOW + "\nThank you for shopping!" + Style.RESET_ALL)
                break
            
            category_index = int(choice) - 1
            
            if 0 <= category_index < len(CATEGORIES):
                selected_category = CATEGORIES[category_index]["name"]
                clear_screen()
                display_banner()
                print(f"\n{Fore.GREEN}You selected: {selected_category}{Style.RESET_ALL}\n")
                # Display products for the selected category
                display_products(selected_category)
            else:
                print(Fore.RED + "\n Invalid category. Please try again." + Style.RESET_ALL)
        
        except ValueError:
            print(Fore.RED + "\n Please enter a valid number." + Style.RESET_ALL)

# Display products for the selected category
def display_products(category_name):
    if category_name in PRODUCTS:
        print(Fore.WHITE + f"Products in {category_name}:\n" + Style.RESET_ALL)
        for product in PRODUCTS[category_name]:
            print(f"ID: {product['id']}, Name: {product['name']}, Price: ${product['price']:.2f}")
    else:
        print(Fore.RED + "\nNo products available in this category." + Style.RESET_ALL)

if __name__ == "__main__":
    main()
 