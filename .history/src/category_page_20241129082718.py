import os
from productsDetails import products

# Define categories directly in this file
categories = ["Clothes", "Jewelry", "Appliances", "Toiletries", "Kitchenware"]

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_categories():
    """Display available categories."""
    clear_screen()
    print("\n=== Categories ===")
    for idx, category in enumerate(categories, start=1):
        print(f"{idx}. {category}")
    print("0. Go Back")

def category_page():
    """Allow the user to select a category and navigate to products."""
    while True:
        display_categories()
        choice = input("Select a category by number (0 to go back): ").strip()

        if choice.isdigit():
            choice = int(choice)
            if choice == 0:
                return  # Go back to the homepage
            elif 1 <= choice <= len(categories):
                selected_category = categories[choice - 1]
                product_list_page(selected_category)  # Navigate to products under this category
        else:
            print("Invalid choice. Please try again.")
            input("\nPress Enter to continue...")
