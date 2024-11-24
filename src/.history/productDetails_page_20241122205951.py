import colorama
from colorama import Fore, Style, Back
colorama.init(autoreset=True)

def display_products(category):
    print(Fore.CYAN + "╔" + "═" * 40 + "╗")
    print(f"║       {Fore.YELLOW}{category.upper()} PRODUCTS{Fore.CYAN}       ║")
    print("╚" + "═" * 40 + "╝" + Style.RESET_ALL)
    
    print("\n" + Fore.WHITE + Back.BLACK + " Available Products " + Style.RESET_ALL)
    
    for product in PRODUCTS.get(category, []):
        print(f"{Fore.GREEN}ID:{Style.RESET_ALL} {product['id']} "
              f"{Fore.BLUE}| Name:{Style.RESET_ALL} {product['name']} "
              f"{Fore.MAGENTA}| Price:{Style.RESET_ALL} ${product['price']}")
    
    input(f"\n{Fore.YELLOW}Press Enter to go back...{Style.RESET_ALL}")

from Products_page import PRODUCTS, main as category_selection, clear_screen, display_banner

def main():
    while True:
        selected_category = category_selection()
        
        if selected_category is None:
            break
        
        clear_screen()
        display_banner()
        
        display_products(selected_category)

if __name__ == "__main__":
    main()