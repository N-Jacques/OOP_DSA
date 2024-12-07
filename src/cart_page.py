# cart_page.py

import uuid
from datetime import datetime

# Static list of products (as dummy data)

products = {
    "T-shirt": 299.99,
    "Gold Ring": 999.99,
    "Rice Cooker": 1499.99,
    "Shampoo": 199.99,
    "Frying Pan": 599.99
}

# Dummy cart with some pre-added products
cart = {
    "T-shirt": 2,
    "Rice Cooker": 1,
    "Shampoo": 3
}

def generate_id(prefix):
    """Generate a unique ID with a given prefix."""
    return f"{prefix}_{uuid.uuid4().hex[:8].upper()}"

# This is the main cart_page
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

    cart_id = generate_id("CART")
    print(f"Cart ID: {cart_id}")

    # Generate order_id
    order_id = generate_id("ORDER")
    print(f"Order ID: {order_id}")

    # Capture order date
    order_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Order Date: {order_date}")

    # Add order status
    order_status = "Pending"
    print(f"Order Status: {order_status}")

    # Handle user-provided address ID
    address_id = input("\nPlease enter your Address ID: ").strip()

    # Display summary
    print("\nOrder Summary:")
    print(f"Order ID: {order_id}")
    print(f"Cart ID: {cart_id}")
    print(f"Order Date: {order_date}")
    print(f"Order Status: {order_status}")
    print(f"Total Amount: ₱{total_cost:,.2f}")
    print(f"Address ID: {address_id}")

# Choices that can be made in cart_page
    while True:
        proceed = input("\nDo you want to proceed to checkout? (yes/no): ").strip().lower()
        if proceed == "yes":
            from src.checkout_page import checkout
            checkout(cart, total_cost)
            break
        elif proceed == "no":
            print("Returning to the previous page.")
            break
        else:
            print("Invalid input. Please type 'yes' or 'no'.")
