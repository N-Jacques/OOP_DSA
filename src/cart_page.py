# cart_page.py
from datetime import datetime
import sqlite3

db_path = "./database/data.db"

# This is the main cart_page
def view_cart(user_id):
    user_data = sqlite3.connect(db_path)
    cart_cursor = user_data.cursor()
    
    # Step 1: Retrieve the cart for the logged-in user
    query = "SELECT cart_id FROM Cart WHERE user_id = ?"
    cart_cursor.execute(query, (user_id,))
    cart = cart_cursor.fetchone()
    
    if cart is None:
        print("You don't have a cart yet.")
        return "empty"  # User doesn't have a cart
    
    cart_id = cart[0]
    
    # Step 2: Retrieve the cart items using INNER JOIN
    cart_item_cursor = user_data.cursor()
    query = """
    SELECT 
        Cart_Items.cart_item_id, 
        Cart_Items.quantity, 
        Cart_Items.total_price, 
        Product_Color.color, 
        Cart_Items.price
    FROM Cart_Items
    INNER JOIN Product_Color ON Cart_Items.product_color_id = Product_Color.product_color_id
    WHERE Cart_Items.cart_id = ?
    """
    cart_item_cursor.execute(query, (cart_id,))
    cart_items = cart_item_cursor.fetchall()
    
    if not cart_items:
        print("Your cart is empty.")
        return "empty"  # No items in the cart
    
    # Step 3: Display the cart items
    total_cost = 0
    print("\nYour Cart Items:")
    for idx, item in enumerate(cart_items, start=1):
        cart_item_id, quantity, total_price, color, price = item
        total_cost += total_price
        print(f"{idx}. Color: {color}, Price: Php  {price:.2f}, Quantity: {quantity}, Total: Php {total_price:.2f}")
    
    print(f"\nTotal Cost: Php {total_cost:.2f}")

    # Step 4: Ask if the user wants to proceed to checkout
    while True:
        proceed = input("\nDo you want to proceed to checkout? (yes/no): ").strip().lower()
        if proceed == "yes":
            from src.checkout_page import checkout
            checkout(cart_id, total_cost)
            return "checkout"
        elif proceed == "no":
            print("Returning to the previous page.")
            return "exit"
        else:
            print("Invalid input. Please type 'yes' or 'no'.")

# Function to clear the cart after checkout
def clear_cart(cart_id):
    """Remove all items from the cart."""
    user_data = sqlite3.connect(db_path)
    cart_cursor = user_data.cursor()

    # Delete items from the cart
    cart_cursor.execute("DELETE FROM Cart_Items WHERE cart_id = ?", (cart_id,))
    user_data.commit()
    print("\nCart items have been removed after checkout.")