import sqlite3
import os
from datetime import datetime
import uuid

# Database path
db_path = "./database/data.db"

# Check if the database file exists
if not os.path.exists(db_path):
    raise FileNotFoundError(f"Database file not found at {db_path}")

# Function to fetch cart details
def fetch_cart_details(cart_id):
    """Fetch cart details including items and calculate total cost."""
    with sqlite3.connect(db_path) as user_data:
        cursor = user_data.cursor()
        query = """
        SELECT ci.cart_item_id, p.product_name, pc.color, ci.price, ci.quantity, ci.total_price
        FROM Cart_Items ci
        JOIN Product_Color pc ON ci.product_color_id = pc.product_color_id
        JOIN Product p ON pc.product_id = p.product_id
        WHERE ci.cart_id = ?
        """
        cursor.execute(query, (cart_id,))
        cart_items = cursor.fetchall()
        total_cost = sum(item[5] for item in cart_items) if cart_items else 0
        return cart_items, total_cost

# Function to fetch user's address
def fetch_user_address(user_id):
    """Fetch the address of the user."""
    with sqlite3.connect(db_path) as user_data:
        cursor = user_data.cursor()
        query = "SELECT address FROM User WHERE user_id = ?"
        cursor.execute(query, (user_id,))
        address = cursor.fetchone()
        return address[0] if address else "Address not found. Please update your profile."

# Function to display cart contents and calculate total cost
def view_cart(cart_items, total_cost):
    """Display the cart contents in a table-like format."""
    if not cart_items:
        print("\nYour cart is empty.")
        return

    print("\nYour Cart:")
    print("=" * 80)
    print(f"{'No.':<5}{'Product Name':<30}{'Color':<15}{'Price':<12}{'Quantity':<10}{'Total Price':<15}")
    print("-" * 80)

    for item_ctr, item in enumerate(cart_items, start=1):
        _, product_name, color, price, quantity, total_price = item
        print(f"{item_ctr:<5}{product_name:<30}{color:<15}{price:>12,.2f}{quantity:>10}{total_price:>15,.2f}")

    print("=" * 80)
    print(f"{'Subtotal:':<60}₱{total_cost:,.2f}")

# Function to update cart item quantity
def update_cart_item(cart_item_id, new_quantity):
    """Update the quantity of a specific item in the cart."""
    with sqlite3.connect(db_path) as user_data:
        cursor = user_data.cursor()
        if new_quantity > 0:
            # Update quantity and total price
            query = """
            UPDATE Cart_Items
            SET quantity = ?, total_price = price * ?
            WHERE cart_item_id = ?
            """
            cursor.execute(query, (new_quantity, new_quantity, cart_item_id))
            print("Quantity updated successfully.")
        else:
            # Remove item if quantity is set to 0
            remove_item(cart_item_id)

# Function to remove an item from the cart
def remove_item(cart_item_id):
    """Remove a specific item from the cart."""
    with sqlite3.connect(db_path) as user_data:
        cursor = user_data.cursor()
        query = "DELETE FROM Cart_Items WHERE cart_item_id = ?"
        cursor.execute(query, (cart_item_id,))
        print("Item removed from the cart.")

# Checkout function
def checkout(user_id, cart_id):
    """Simulate checkout process."""
    print("\nCheckout Process:")
    address = fetch_user_address(user_id)
    print(f"User Address: {address}")

    while True:
        cart_items, total_cost = fetch_cart_details(cart_id)
        if not cart_items:
            print("Your cart is empty. Cannot proceed to checkout.")
            return

        print("\nOrder Summary:")
        view_cart(cart_items, total_cost)

        # Ask user if they want to modify the cart
        modify_cart = input("\nDo you want to modify your cart? (yes/no): ").strip().lower()
        if modify_cart == "yes":
            try:
                item_no = int(input("Enter the item number you want to modify (or 0 to skip): "))
                if item_no == 0:
                    break  # Skip modification
                if 1 <= item_no <= len(cart_items):
                    cart_item_id = cart_items[item_no - 1][0]
                    action = input("Enter 'update' to change quantity or 'remove' to remove the item: ").strip().lower()
                    if action == "update":
                        new_quantity = int(input("Enter the new quantity: "))
                        update_cart_item(cart_item_id, new_quantity)
                    elif action == "remove":
                        remove_item(cart_item_id)
                    else:
                        print("Invalid action.")
                else:
                    print("Invalid item number.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif modify_cart == "no":
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

    # Final confirmation to proceed to checkout
    while True:
        confirm = input("\nConfirm checkout? (yes/no): ").strip().lower()
        if confirm == "yes":
            place_order(user_id, cart_id, total_cost)
            break
        elif confirm == "no":
            print("Checkout cancelled.")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

# Function to place an order
def place_order(user_id, cart_id, total_cost):
    """Finalize the order and save to database."""
    with sqlite3.connect(db_path) as user_data:
        cursor = user_data.cursor()
        
        # Generate a unique order ID
        order_id = uuid.uuid4().hex  # Shorter UUID for readability
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Insert order into the Orders table
        query = """
        INSERT INTO Orders (order_id, user_id, cart_id, total_cost, timestamp)
        VALUES (?, ?, ?, ?, ?)
        """
        cursor.execute(query, (order_id, user_id, cart_id, total_cost, timestamp))
        
        # Clear the cart after placing the order
        clear_cart(cart_id)
        
        print(f"\nOrder placed successfully! Order ID: {order_id}")
        print(f"Total Amount: ₱{total_cost:,.2f}")
        print(f"Order Timestamp: {timestamp}")

# Function to clear the cart
def clear_cart(cart_id):
    """Remove all items from the cart after checkout."""
    with sqlite3.connect(db_path) as user_data:
        cursor = user_data.cursor()
        query = "DELETE FROM Cart_Items WHERE cart_id = ?"
        cursor.execute(query, (cart_id,))
        print("Cart cleared successfully.")

# Function to initiate cart page with user_id
def cart_page(user_id):
    """Display the cart page and allow the user to manage cart items."""
    cart_id = get_cart_id(user_id)
    if cart_id:
        cart_actions(cart_id, user_id)
    else:
        print("No cart found. Please add items to your cart before proceeding.")

# Function to get user's cart_id
def get_cart_id(user_id):
    """Fetch the cart_id for the given user."""
    with sqlite3.connect(db_path) as user_data:
        cursor = user_data.cursor()
        query = "SELECT cart_id FROM Cart WHERE user_id = ?"
        cursor.execute(query, (user_id,))
        cart = cursor.fetchone()
        return cart[0] if cart else None

# Function to handle cart actions
def cart_actions(cart_id, user_id):
    """Display cart and proceed to checkout."""
    cart_items, total_cost = fetch_cart_details(cart_id)
    if not cart_items:
        print("Your cart is empty.")
    else:
        view_cart(cart_items, total_cost)
        print("\nProceeding to checkout...")
        checkout(user_id, cart_id)
