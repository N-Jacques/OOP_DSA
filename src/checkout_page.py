# checkout_page.py

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

# Function to display cart contents and calculate total cost
def view_cart(cart):
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

# Function to apply discounts based on the total cost
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

# Function to handle the checkout process
def checkout(cart):
    """Checkout and generate receipt."""
    print("\nCheckout:")
    if not cart:
        print("Your cart is empty. Add items before checking out.")
        return

    # View cart and calculate totals
    total_cost = view_cart(cart)
    discount = apply_discounts(total_cost)
    final_total = total_cost - discount

    # Generate unique IDs and other order details
    order_id = str(uuid.uuid4())
    cart_id = str(uuid.uuid4())
    address_id = str(uuid.uuid4())
    order_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    order_status = "Pending"
    amount_paid = final_total

    print(f"Cart ID: {cart_id}")
    print(f"Final Total: ₱{final_total:,.2f}")

    while True:
        confirm = input("Proceed with payment? (yes/no): ").strip().lower()
        if confirm == "yes":
            order_status = "Paid"
            print("\nPayment successful! Here's your receipt:")
            generate_receipt(cart, final_total, discount, order_id, cart_id, address_id, order_date, order_status, amount_paid)
            break
        elif confirm == "no":
            print("\nPayment canceled.")
            break
        else:
            print("Invalid input. Please type 'yes' or 'no'.")

# Function to generate and display the receipt
def generate_receipt(cart, total, discount, order_id, cart_id, address_id, order_date, order_status, amount_paid):
    """Generate and display receipt after successful payment."""
    print("\nReceipt:")
    print("=" * 30)
    print(f"Order ID: {order_id}")
    print(f"Cart ID: {cart_id}")
    print(f"Order Date: {order_date}")
    print(f"Order Status: {order_status}")
    print(f"Address ID: {address_id}")
    for product, quantity in cart.items():
        cost = products[product] * quantity
        print(f"{product}: {quantity} x ₱{products[product]:,.2f} = ₱{cost:,.2f}")
    print("-" * 30)
    print(f"Subtotal: ₱{total + discount:,.2f}")
    print(f"Discount: -₱{discount:,.2f}")
    print(f"Total Paid: ₱{amount_paid:,.2f}")
    print("=" * 30)
    print("Thank you for shopping with us!")
