import os
from productsDetails import products

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_products(category=None):
    """Display products, optionally filtered by category."""
    clear_screen()
    if category:
        print(f"\n=== Products in {category} ===")
        filtered_products = {k: v for k, v in products.items() if v["category"] == category}
    else:
        print("\n=== All Products ===")
        filtered_products = products

    print(f"{'ID':<10}{'Name':<20}{'Price':<10}{'Stock':<10}")
    print("-" * 50)
    for pid, details in filtered_products.items():
        print(f"{pid:<10}{details['name']:<20}₱{details['price']:<10}{details['stock']:<10}")

    return filtered_products

def product_selection(filtered_products):
    """Allow the user to select a product by ID."""
    while True:
        product_id = input("Enter the Product ID to view details (or 0 to go back): ").strip()
        if product_id == "0":
            return None
        if product_id in filtered_products:
            return product_id
        print("Invalid Product ID. Please try again.")
