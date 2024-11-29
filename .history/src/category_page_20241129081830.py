import os

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

def category_selection():
    """Allow the user to select a category."""
    while True:
        display_categories()
        choice = input("Select a category by number (0 to go back): ")

        if choice.isdigit():
            choice = int(choice)
            if choice == 0:
                return None
            elif 1 <= choice <= len(categories):
                return categories[choice - 1]
        print("Invalid choice. Please try again.")
