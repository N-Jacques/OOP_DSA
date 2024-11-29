# cart_page.py

# Static list of products (as dummy data)
products = {
    "T-shirt": 299.99,
    "Gold Ring": 999.99,
    "Rice Cooker": 1499.99,
    "Shampoo": 199.99,
    "Frying Pan": 599.99
}

# Dummy cart to store products added
cart = {}

def display_products():
    """Display available products."""
    print("\nAvailable Products:")
    for product, price in products.items():
        print(f"{product}: ₱{price:,.2f}")

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
    """View the contents of the cart."""
    if not cart:
        print("\nYour cart is empty.")
    else:
        print("\nYour Cart:")
        total_cost = 0
        for product, quantity in cart.items():
            cost = products[product] * quantity
            total_cost += cost
            print(f"{product}: {quantity} x ₱{products[product]:,.2f} = ₱{cost:,.2f}")
        print(f"\nTotal Cost: ₱{total_cost:,.2f}")
