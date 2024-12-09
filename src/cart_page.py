import sqlite3
import os
import time

db_path = "./database/data.db"

def clear_screen(): #clears screen
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

    # connect program to linked data 
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
    
    while True:
        # Step 2: Retrieve the cart items with their details
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
        cart_cursor.execute(query, (cart_id,))
        cart_items = cart_cursor.fetchall()

        if not cart_items:
            print("Your cart is empty.")
            return "empty"  # No items in the cart

        # Step 3: Display the cart items in a table format
        total_cost = 0
        print("\nYour Cart Items:")
        print(f"{'Item ID':<10} {'Color':<10} {'Price ($)':<12} {'Quantity':<10} {'Total Price ($)':<15}")
        
        for item in cart_items:
            cart_item_id, quantity, total_price, color, price = item
            total_cost += total_price
            print(f"{cart_item_id:<10} {color:<10} {price:<12.2f} {quantity:<10} {total_price:<15.2f}")
        
        print(f"\n{'Total Cost':<42} ${total_cost:.2f}")
        print(f"{'Total Items':<42} {len(cart_items)}")

        # Step 4: Display options for the user
        print("\nOptions:")
        print("1. Change Quantity")
        print("2. Remove an Item")
        print("3. Proceed to Checkout")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            # Change quantity
            item_id = int(input("Enter the Item ID to change quantity: ").strip())
            new_quantity = int(input("Enter the new quantity: ").strip())
            change_quantity(cart_id, item_id, new_quantity, cart_cursor, user_data)
        elif choice == "2":
            # Remove item
            item_id = int(input("Enter the Item ID to remove: ").strip())
            remove_item(cart_id, item_id, cart_cursor, user_data)
        elif choice == "3":
            # Proceed to checkout
            from src.checkout_page import checkout
            checkout(cart_id, total_cost)
            return "checkout"
        elif choice == "4":
            print("Returning to the previous page.")
            return "exit"
        else:
            print("Invalid input. Please choose a valid option.")

# Function to change the quantity of a cart item
def change_quantity(cart_id, item_id, new_quantity, cursor, connection):
    if new_quantity <= 0:
        print("Quantity must be greater than zero. Use 'Remove an Item' option to delete an item.") 
        return

    # Fetch the item price to recalculate the total price
    query = "SELECT price FROM Cart_Items WHERE cart_item_id = ? AND cart_id = ?"
    cursor.execute(query, (item_id, cart_id))
    item = cursor.fetchone()

    if item:
        price = item[0]
        total_price = price * new_quantity
        # Update the quantity and total price in the database
        update_query = """
        UPDATE Cart_Items
        SET quantity = ?, total_price = ?
        WHERE cart_item_id = ? AND cart_id = ?
        """
        cursor.execute(update_query, (new_quantity, total_price, item_id, cart_id))
        connection.commit()
        print(f"Quantity updated successfully for Item ID {item_id}.")
        time.sleep(1.2)
        clear_screen()
        
    else:
        print("Item not found in the cart.")

# Function to remove an item from the cart
def remove_item(cart_id, item_id, cursor, connection):
    # Delete the item from the cart
    delete_query = "DELETE FROM Cart_Items WHERE cart_item_id = ? AND cart_id = ?"
    cursor.execute(delete_query, (item_id, cart_id))
    connection.commit()
    print(f"Item ID {item_id} removed from the cart.")
