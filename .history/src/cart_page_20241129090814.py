import os

# Define the products and cart as dictionaries
products = {
    "Laptop": 65000,
    "Headphones": 2500,
    "Smartphone": 35000,
    "Keyboard": 1200,
    "Mouse": 800,
}

cart = {}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_products():
    """Display the available products with prices."""
    print("\nAvailable Products:")
    for product, price in products.items():
        print(f"{product}: ₱{price:,}")

def add_to_cart(product, quantity):
    """Add a product to the cart."""
    if product in products:
        if product in cart:
            cart[product] += quantity
        else:
            cart[product] = quantity
        print(f"{quantity} x {product} added to your cart.")
    else:
        print("Product not found. Please select a valid product.")

def view_cart():
    """Display the cart's contents."""
    if not cart:
        print("\nYour cart is empty.")
    else:
        print("\nYour Cart:")
        for product, quantity in cart.items():
            cost = products[product] * quantity
            print(f"{product}: {quantity} x ₱{products[product]:,} = ₱{cost:,}")
