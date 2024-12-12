import sqlite3
import os
import time
from colorama import Fore, Style, init
from datetime import datetime


db_path = "./database/data.db"

def clear_screen():  # clears screen
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def clear_cart(cart_id):
    """Clear the items from the cart in the database."""
    try:
        user_data = sqlite3.connect(db_path)
        cursor = user_data.cursor()
        
        # Delete items from Cart_Items table
        delete_query = "DELETE FROM Cart_Items WHERE cart_id = ?"
        cursor.execute(delete_query, (cart_id,))
        user_data.commit()
        print(Fore.GREEN + "Cart items cleared successfully.")
    except sqlite3.Error as e:
        print(Fore.RED + f"Error clearing cart: {e}")
    finally:
        user_data.close()

def checkout(cart_id, user_id, total_cost):
    """Handle the checkout process."""
    user_data = sqlite3.connect(db_path)
    cursor = user_data.cursor()

    # Step 1: Fetch user information (address) from the User table
    query = "SELECT first_name, last_name, address FROM User WHERE user_id = ?"
    cursor.execute(query, (user_id,))
    user_info = cursor.fetchone()

    if user_info is None:
        print(Fore.RED + Style.BRIGHT + "User not found.")
        return

    first_name, last_name, address = user_info

    # Step 2: Display order summary
    clear_screen()
    print(Fore.GREEN + "=" * 39)
    print(Fore.YELLOW + Style.BRIGHT + "██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗ ██████╗ ██╗   ██╗████████╗")
    print(Fore.YELLOW + Style.BRIGHT + "██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔═══██╗██║   ██║╚══██╔══╝")
    print(Fore.YELLOW + Style.BRIGHT + "██║     ███████║█████╗  ██║     █████╔╝ ██║   ██║██║   ██║   ██║   ")
    print(Fore.YELLOW + Style.BRIGHT + "██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██║   ██║██║   ██║   ██║   ")
    print(Fore.YELLOW + Style.BRIGHT + "╚██████╗██║  ██║███████╗╚██████╗██║  ██╗╚██████╔╝╚██████╔╝   ██║   ")
    print(Fore.YELLOW + Style.BRIGHT + " ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝    ╚═╝   ")

    print(Fore.GREEN + "=" * 39)
    print("\nYour Cart Items:")
    print("=" * 85)

    # Step 3: Retrieve the cart items for the user and display them
    query = """
    SELECT 
        Cart_Items.cart_item_id, 
        Product.product_name, 
        Cart_Items.quantity, 
        Cart_Items.total_price, 
        Product_Color.color, 
        Cart_Items.price
    FROM Cart_Items
    INNER JOIN Product_Color ON Cart_Items.product_color_id = Product_Color.product_color_id
    INNER JOIN Product ON Product_Color.product_id = Product.product_id
    WHERE Cart_Items.cart_id = ?
    """
    cursor.execute(query, (cart_id,))
    cart_items = cursor.fetchall()

    if not cart_items:
        print("Your cart is empty.")
        return

    total_cost = 0
    for item in cart_items:
        cart_item_id, product_name, quantity, total_price, color, price = item
        total_cost += total_price
        print(f"{cart_item_id:<10} {product_name:<20} {color:<10} {price:<12.2f} {quantity:<10} {total_price:<15.2f}")

    print("=" * 85)
    print(f"\nTotal Cost: Php{total_cost:.2f}")
    print(f"Total Items: {len(cart_items)}")
    
    # Step 4: Show shipping address
    print("\nShipping Address:")
    print("-" * 20)
    print(f"{first_name} {last_name}\n{address}")
    print("=" * 20)

    # Step 5: Include shipping fee (hardcoded for simplicity)
    shipping_fee = 40.00
    total_due = total_cost + shipping_fee

    print(f"Shipping Fee: Php{shipping_fee:.2f}")
    print(f"Total Due (after shipping): Php{total_due:.2f}")

    # Step 6: Payment method (using default method)
    payment_method = "Cash on Delivery"
    print(f"Payment Method: {payment_method}")

    # Step 7: Confirm to proceed with payment
    proceed = input("\nProceed with payment? (y/n): ").strip().lower()
    if proceed == "y":
        # Step 8: Insert order into Orders table
        order_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        order_status = "Pending"
        
        insert_order_query = """
        INSERT INTO Orders (user_id, cart_id, address, amount_paid, order_date, order_status)
        VALUES (?, ?, ?, ?, ?, ?)
        """
        cursor.execute(insert_order_query, (user_id, cart_id, address, total_due, order_date, order_status))
        user_data.commit()
        clear_screen()

        # Step 9: Display order confirmation
        order_id = cursor.lastrowid
        print("\n" + "=" * 39)
        print(Fore.GREEN + "Checkout Complete! Your order has been successfully placed.")
        print("=" * 39)
        print("\nOrder Details:")
        print("-" * 20)
        print(f"Order ID: {order_id}")
        print(f"Order Date: {order_date}")
        print(f"Order Status: {order_status}")
        print(f"Shipping Address: {address}")
        
        print("\nItems Ordered:")
        for item in cart_items:
            product_name, quantity = item[1], item[2]
            print(f"{product_name} (Quantity: {quantity})")
        
        print(f"\nTotal Amount Paid: Php{total_due:.2f}")
        print("\nThank you for shopping with us!")
        
        time.sleep(2)
        clear_cart(cart_id)
    else:
        print("Checkout cancelled.")
