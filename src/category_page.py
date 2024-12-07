import os
import sqlite3
from src.products_page import display_products, product_selection
from src.productDetails_page import display_product_details

db_path = "./database/data.db"  # Path to your SQLite database

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_categories():
    """Fetch unique categories from the database."""
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT DISTINCT category FROM product")
        categories = [row[0] for row in cursor.fetchall()]
        conn.close()
        return categories
    except sqlite3.Error as e:
        print(f"Error accessing the database: {e}")
        return []

def display_categories(categories):
    """Display available categories."""
    clear_screen()
    print("\n=== Categories ===")
    for idx, category in enumerate(categories, start=1):
        print(f"{idx}. {category}")
    print("0. Go Back")

def category_page():
    """Allow the user to select a category and view products."""
    while True:
        categories = get_categories()
        if not categories:
            print("No categories found in the database.")
            input("\nPress Enter to return to the main menu...")
            return
        
        display_categories(categories)
        choice = input("Select a category by number (0 to go back): ").strip()

        if choice.isdigit():
            choice = int(choice)
            if choice == 0:
                return  # Go back to the homepage
            elif 1 <= choice <= len(categories):
                selected_category = categories[choice - 1]
                filtered_products = display_products(selected_category)  # Show products in this category
                product_id = product_selection(filtered_products)  # Let the user select a product

                if product_id:
                    display_product_details(product_id)  # Navigate to product details page
                else:
                    continue
        else:
            print("Invalid choice. Please try again.")
            input("\nPress Enter to continue...")
