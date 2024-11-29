# checkout_page.py

# Static list of products (as dummy data)
products = {
    "T-shirt": 299.99,
    "Gold Ring": 999.99,
    "Rice Cooker": 1499.99,
    "Shampoo": 199.99,
    "Frying Pan": 599.99
}

# Cart passed to the checkout
cart = {
    "T-shirt": 2,  # 2 T-shirts
    "Rice Cooker": 1,  # 1 Rice Cooker
    "Shampoo": 3  # 3 Shampoos
}

def view_cart():
    """Display the cart contents."""
    if not cart:
        print("\nYour cart is empty.")
        return 0
    else:
        print("\nYour Cart:")
        total_cost = 0
        for product, quantity in cart.items():
            cost = products[product] * quantity
            total_cost += cost
            print(f"{product}: {quantity} x ₱{products[product]:,.2f} = ₱{cost:,.2f}")
        print(f"Subtotal: ₱{total_cost:,.2f}")
        return total_cost

def apply_discounts(total):
    """Apply discounts based on total cost."""
    discount = 0
    if total >= 100000:
        discount = total * 0.10
        print(f"Discount applied: ₱{discount:,.2f} (10% off)")
    elif total >= 50000:
        discount = total * 0.05
        print(f"Discount applied: ₱{discount:,.2f} (5% off)")
    return discount

def checkout():
    """Checkout and generate receipt."""
    print("\nCheckout:")
    if not cart:
        print("Your cart is empty. Add items before checking out.")
        return

    total_cost = view_cart()
    discount = apply_discounts(total_cost)
    final_total = total_cost - discount

    print(f"Final Total: ₱{final_total:,.2f}")
    while True:
        confirm = input("Proceed with payment? (yes/no): ").strip().lower()
        if confirm == "yes":
            print("\nPayment successful! Here's your receipt:")
            generate_receipt(final_total, discount)
            break
        elif confirm == "no":
            print("\nPayment canceled.")
            break
        else:
            print("Invalid input. Please type 'yes' or 'no'.")

def generate_receipt(total, discount):
    """Generate and display receipt after successful payment."""
    print("\nReceipt:")
    print("=" * 30)
    for product, quantity in cart.items():
        cost = products[product] * quantity
        print(f"{product}: {quantity} x ₱{products[product]:,.2f} = ₱{cost:,.2f}")
    print("-" * 30)
    print(f"Subtotal: ₱{total:,.2f}")
    print(f"Discount: -₱{discount:,.2f}")
    print(f"Total Paid: ₱{total:,.2f}")
    print("=" * 30)
    print("Thank you for shopping with us!")
