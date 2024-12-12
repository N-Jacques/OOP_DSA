from datetime import datetime
import sqlite3

db_path = "./database/data.db"

# Function to fetch cart details
def fetch_cart_details(cart_id):
    """Fetch cart details including items and calculate total cost."""
    user_data = sqlite3.connect(db_path)
    cursor = user_data.cursor()

    # Fetch items in the cart
    query = """
    SELECT p.product_name, ci.price, ci.quantity, ci.total_price
    FROM Cart_Items ci
    JOIN Product_Color pc ON ci.product_color_id = pc.product_color_id
    JOIN Product p ON pc.product_id = p.product_id
    WHERE ci.cart_id = ?
    """
    cursor.execute(query, (cart_id,))
    cart_items = cursor.fetchall()

    # Calculate total cost
    total_cost = sum(item[3] for item in cart_items)

    return cart_items, total_cost


# Function to fetch user's address
def fetch_user_address(user_id):
    """Fetch the address of the user."""
    user_data = sqlite3.connect(db_path)
    cursor = user_data.cursor()

    query = """
    SELECT address
    FROM User
    WHERE user_id = ?
    """
    cursor.execute(query, (user_id,))
    address = cursor.fetchone()

    if address:
        return address[0]
    else:
        return "Address not found. Please update your profile."


# Function to display cart contents and calculate total cost
def view_cart(cart_items, total_cost):
    """Display the cart contents."""
    if not cart_items:
        print("\nYour cart is empty.")
    else:
        print("\nYour Cart:")
        for item_number, item in enumerate(cart_items, start=1):
            product_name, price, quantity, total_price = item
            print(f"{item_number}. {product_name}: {quantity} x ₱{price:,.2f} = ₱{total_price:,.2f}")
        print(f"Subtotal: ₱{total_cost:,.2f}")


# Function to handle the checkout process
def checkout(user_id, cart_id):
    """Checkout and generate receipt."""
    print("\nCheckout:")
    
    # Fetch cart details
    cart_items, total_cost = fetch_cart_details(cart_id)

    if not cart_items:
        print("Your cart is empty. Add items before checking out.")
        return

    # View cart and calculate totals
    view_cart(cart_items, total_cost)

    # Fetch user address
    address = fetch_user_address(user_id)
    print(f"\nShipping Address: {address}")

    # Add shipping fee
    shipping_fee = 40.00
    print(f"Shipping Fee: ₱{shipping_fee:,.2f}")

    # Calculate final total
    final_total = total_cost + shipping_fee
    print(f"Total Due (after shipping): ₱{final_total:,.2f}")

    # Fetch payment method (use database value if available)
    payment_method = "Cash"  # Default, but you can query if there are other options

    # Confirm payment
    confirm = input("\nProceed with payment? (y/n): ").strip().lower()

    if confirm == "y":
        # Generate receipt
        order_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        order_status = None

        # Save checkout data
        save_checkout_data(cart_id, address, payment_method, final_total)

        # Insert the order details into the Orders table
        save_order_data(cart_id, user_id, address, final_total, order_date, order_status)

        # Generate receipt
        generate_receipt(cart_items, total_cost, 0, cart_id, address, order_date, order_status, final_total)
        
        print("\nCheckout Complete! You will now be redirected...")
        # You can add any post-checkout logic here (e.g., redirect to another page, etc.)
        
    elif confirm == "n":
        print("\nPayment canceled.")
    else:
        print("Invalid input. Please type 'y' or 'n'.")


# Function to save checkout data into the database
def save_checkout_data(cart_id, address, payment_method, total_due):
    """Save checkout details to the database."""
    user_data = sqlite3.connect(db_path)
    cursor = user_data.cursor()

    query = """
    INSERT INTO Checkout (cart_id, address, payment_method, total_due)
    VALUES (?, ?, ?, ?)
    """
    cursor.execute(query, (cart_id, address, payment_method, total_due))
    user_data.commit()
    print("\nCheckout data saved successfully!")


# Function to generate and display the receipt
def generate_receipt(cart_items, total, discount, cart_id, address, order_date, order_status, amount_paid):
    """Generate and display receipt after successful payment."""
    print("\nReceipt:")
    print("=" * 30)
    print(f"Cart ID: {cart_id}")
    print(f"Order Date: {order_date}")
    print(f"Order Status: {order_status}")
    print(f"Shipping Address: {address}")
    for item_number, item in enumerate(cart_items, start=1):
        product_name, price, quantity, total_price = item
        print(f"{item_number}. {product_name}: {quantity} x ₱{price:,.2f} = ₱{total_price:,.2f}")
    print("-" * 30)
    print(f"Subtotal: ₱{total + discount:,.2f}")
    print(f"Discount: -₱{discount:,.2f}")
    print(f"Total Paid: ₱{amount_paid:,.2f}")
    print("=" * 30)
    print("Thank you for shopping with us!")


# Function to save order data into the Orders table
def save_order_data(cart_id, user_id, address, amount_paid, order_date, order_status):
    """Save order details to the Orders table."""
    user_data = sqlite3.connect(db_path)
    cursor = user_data.cursor()

    query = """
    INSERT INTO Orders (cart_id, order_date, order_status, amount_paid, address, user_id)
    VALUES (?, ?, ?, ?, ?, ?)
    """
    cursor.execute(query, (cart_id, order_date, order_status, amount_paid, address, user_id))
    user_data.commit()
    print("\nOrder data saved successfully!")


# Simulate running the checkout process
def cart_page(user_id, cart_id):
    """Simulate displaying the cart page."""
    print("Displaying cart page...")
    checkout(user_id, cart_id)  # Proceed to checkout after viewing the cart.


