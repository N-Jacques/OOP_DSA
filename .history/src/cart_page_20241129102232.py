# cart_page.py

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
    "T-shirt": 2,  # 2 T-shirts
    "Rice Cooker": 1,  # 1 Rice Cooker
    "Shampoo": 3  # 3 Shampoos
}

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

    # Option to proceed to checkout
    while True:
        proceed = input("\nDo you want to proceed to checkout? (yes/no): ").strip().lower()
        if proceed == "yes":
            from src.checkout_page import checkout  # Import checkout when needed
            checkout(cart, total_cost)  # Proceed to checkout, passing cart and total_cost
            break
        elif proceed == "no":
            print("Returning to the previous page.")
            break
        else:
            print("Invalid input. Please type 'yes' or 'no'.")
