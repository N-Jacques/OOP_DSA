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

def view_cart():
    """Display the cart contents."""
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
