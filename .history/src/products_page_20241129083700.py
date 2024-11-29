import os
from productsDetails import products
from productDetails_page import display_product_details

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

def add_to_cart(product_id):
    """Simulate adding a product to the cart."""
    print(f"Product {product_id} added to cart!")

def products_page(category=None):
    """Main function to display products and handle product selection."""
    filtered_products = display_products(category)  # Display products (either all or by category)

    # Allow the user to select a product
    product_id = product_selection(filtered_products)

    if product_id:
        display_product_details(product_id)  # Navigate to product details page

        # After showing product details, give the option to add to cart or go back
        while True:
            action = input(f"Product {product_id} added to cart! (Press 'Enter' to continue or '0' to go back): ").strip()
            if action == "0":
                return
            elif action == "":
                add_to_cart(product_id)
                return
            else:
                print("Invalid input. Please try again.")