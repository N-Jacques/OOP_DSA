import os

# Define the products dictionary directly in this file
products = {
    "P001": {"name": "T-shirt", "price": 299.99, "category": "Clothes", "stock": 50},
    "P002": {"name": "Gold Ring", "price": 999.99, "category": "Jewelry", "stock": 20},
    "P003": {"name": "Rice Cooker", "price": 1499.99, "category": "Appliances", "stock": 30},
    "P004": {"name": "Shampoo", "price": 199.99, "category": "Toiletries", "stock": 100},
    "P005": {"name": "Frying Pan", "price": 599.99, "category": "Kitchenware", "stock": 40}
}

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
    return product_id  # Return the selected product's ID for further action (e.g., add to cart)
