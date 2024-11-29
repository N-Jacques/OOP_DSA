import os
from productsDetails import products

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_product_details(product_id):
    """Display details for a selected product."""
    product = products.get(product_id)
    if not product:
        print("Product not found.")
        return

    clear_screen()
    print("\n=== Product Details ===")
    print(f"Name: {product['name']}")
    print(f"Price: ₱{product['price']}")
    print(f"Category: {product['category']}")
    print(f"Stock: {product['stock']}")

    input("\nPress Enter to go back...")
