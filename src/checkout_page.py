# checkout_page.py


from datetime import datetime
import sqlite3

# Function to display cart contents and calculate total cost
def view_cart(cart, total_cost):
    """Display the cart contents."""
    if not cart:
        print("\nYour cart is empty.")
        return 0
    else:
        print("\nYour Cart:")
        total_cost = 0
        for product, quantity in cart.items():
            cost = product[product] * quantity
            total_cost += cost
            print(f"{product}: {quantity} x ₱{product[product]:,.2f} = ₱{cost:,.2f}")
        print(f"Subtotal: ₱{total_cost:,.2f}")
        return total_cost

# Function to handle the checkout process
def checkout(cart_id, total cost):
    """Checkout and generate receipt."""
    print("\nCheckout:")
    if not cart_id:
        print("Your cart is empty. Add items before checking out.")
        return

    # View cart and calculate totals
    total_cost = view_cart(cart)
    final_total = total_cost 

    # Add shipping fee
    shipping_fee = 40.00
    print(f"Shipping Fee: ₱{shipping_fee:,.2f}")

    # Calculate final total
    final_total = total_cost - shipping_fee
    print(f"Total Due (after shipping): ₱{final_total:,.2f}")

    
    print(f"Cart ID: {cart_id}")
    print(f"Final Total: ₱{final_total:,.2f}")

    while True:
        confirm = input("Proceed with payment? (yes/no): ").strip().lower()
        if confirm == "yes":
            order_status = "Paid"
            print("\nPayment successful! Here's your receipt:")
            generate_receipt(cart, final_total, order_id, cart_id, address_id, order_date, order_status, amount_paid)
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
        cost = product[product] * quantity
        print(f"{product}: {quantity} x ₱{product[product]:,.2f} = ₱{cost:,.2f}")
    print("-" * 30)
    print(f"Subtotal: ₱{total + discount:,.2f}")
    print(f"Discount: -₱{discount:,.2f}")
    print(f"Total Paid: ₱{amount_paid:,.2f}")
    print("=" * 30)
    print("Thank you for shopping with us!")
