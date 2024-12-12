import os
import sqlite3
from typing import Dict, Optional
from colorama import Fore, Style, init

db_path = "./database/data.db"

def clear_screen() -> None:
    """Clear the console screen across different operating systems."""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_product_details(product_id: str) -> Optional[Dict[str, str]]:
    """
    Fetch the details of a single product from the database.
    
    Args:
        product_id (str): Unique identifier of the product.
    
    Returns:
        Dict of product details or None if not found.
    """
    try:
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT p.category, p.product_name, p.full_description, GROUP_CONCAT(pc.color, ', ') as colors, pc.price, pc.stock
                FROM product p JOIN product_color pc ON p.product_id = pc.product_id 
                WHERE p.product_id = ? 
                GROUP BY p.product_id
            """, (product_id,))
            product_details = cursor.fetchone()

            if product_details:
                return {
                    "category": product_details[0],
                    "product_name": product_details[1],
                    "full_description": product_details[2],
                    "colors": product_details[3],
                    "price": product_details[4],
                    "stock": product_details[5]
                }
            return None
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        input("Press Enter to continue...")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        input("Press Enter to continue...")
        return None

def add_to_cart(product_id: str, user_id: int):
    """Add the selected product and quantity to the user's cart."""
    try:
        quantity = int(input("Enter quantity to add to cart: "))

        # Validate quantity
        if quantity <= 0:
            print("Quantity must be greater than 0.")
            return

        # Fetch product details
        product_details = get_product_details(product_id)
        price = float(product_details['price'])

        # Connect to the database
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()

            # Check if the user has an existing cart
            cursor.execute("SELECT cart_id FROM Cart WHERE user_id = ?", (user_id,))
            cart = cursor.fetchone()

            if cart:
                cart_id = cart[0]
            else:
                # If no cart exists, create one
                cursor.execute("INSERT INTO Cart (user_id) VALUES (?)", (user_id,))
                conn.commit()
                cart_id = cursor.lastrowid

            # Fetch the product_color_id for the selected product
            cursor.execute("""
                SELECT product_color_id 
                FROM Product_Color 
                WHERE product_id = ? 
                LIMIT 1
            """, (product_id,))
            product_color_id = cursor.fetchone()

            if not product_color_id:
                print(f"Product color for product {product_id} not found.")
                return

            product_color_id = product_color_id[0]

            # Add the item to the Cart_Items table
            cursor.execute("""
                INSERT INTO Cart_Items (cart_id, product_color_id, quantity, price, total_price)
                VALUES (?, ?, ?, ?, ?)
            """, (cart_id, product_color_id, quantity, price, quantity * price))

            conn.commit()

            print(f"{quantity} of {product_details['product_name']} successfully added to your cart!")
            input("Press Enter to continue...")

            # Return to the category page
            from src.category_page import category_page
            category_page(user_id)  # Pass user_id back to the category page

    except ValueError:
        print("Please enter a valid number for quantity.")
    except sqlite3.Error as e:
        print(f"Error adding to cart: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

def display_product_details(product_id: str, user_id: int) -> None:
    """
    Display the details of a selected product and handle adding to cart.
    
    Args:
        product_id (str): Unique identifier of the product.
        user_id (int): Unique identifier of the user.
    """
    while True:
        product_details = get_product_details(product_id)

        clear_screen()
        
        print(Fore.YELLOW + Style.BRIGHT +" ██████╗ ██████╗  ██████╗ ██████╗ ██╗   ██╗ ██████╗████████╗    ██████╗ ███████╗████████╗ █████╗ ██╗██╗     ███████╗")
        print(Fore.YELLOW + Style.BRIGHT +" ██╔══██╗██╔══██╗██╔═══██╗██╔══██╗██║   ██║██╔════╝╚══██╔══╝    ██╔══██╗██╔════╝╚══██╔══╝██╔══██╗██║██║     ██╔════╝")
        print(Fore.YELLOW + Style.BRIGHT +" ██████╔╝██████╔╝██║   ██║██║  ██║██║   ██║██║        ██║       ██║  ██║█████╗     ██║   ███████║██║██║     ███████╗")
        print(Fore.YELLOW + Style.BRIGHT +" ██╔═══╝ ██╔══██╗██║   ██║██║  ██║██║   ██║██║        ██║       ██║  ██║██╔══╝     ██║   ██╔══██║██║██║     ╚════██║")
        print(Fore.YELLOW + Style.BRIGHT +" ██║     ██║  ██║╚██████╔╝██████╔╝╚██████╔╝╚██████╗   ██║       ██████╔╝███████╗   ██║   ██║  ██║██║███████╗███████║")
        print(Fore.YELLOW + Style.BRIGHT +" ╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═════╝  ╚═════╝  ╚═════╝   ╚═╝       ╚═════╝ ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝╚══════╝╚══════╝")  
        print(Fore.GREEN + Style.BRIGHT +"=" * 110)
        print(f"Category: {product_details['category']}")
        print(f"Product Name: {product_details['product_name']}")
        print(f"Description: {product_details['full_description']}")
        print(f"Color: {product_details['colors']}")
        print(f"Price: ₱{product_details['price']}")
        print(f"Stock: {product_details['stock']}")
        print(Fore.GREEN + Style.BRIGHT +"=" * 110)
        print()
        add_to_cart_choice = input("Do you want to add this product to your cart? (yes/no): ").strip().lower()
        print()

        if add_to_cart_choice == 'yes':
            print()
            add_to_cart(product_id, user_id)  # Call add_to_cart and pass user_id

        elif add_to_cart_choice == 'no':
            return

    