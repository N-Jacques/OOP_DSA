import os
import sqlite3
from typing import Dict, Optional

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
            
            # Fetch all available color variants for the product
            cursor.execute("""
                SELECT p.category, p.product_name, p.short_description, 
                       GROUP_CONCAT(pc.color, ', ') as colors,
                       pc.price, pc.stock
                FROM product p
                JOIN product_color pc ON p.product_id = pc.product_id
                WHERE p.product_id = ?
                GROUP BY p.product_id
            """, (product_id,))
            
            product_details = cursor.fetchone()

            if product_details:
                return {
                    "product_name": product_details[1],
                    "short_description": product_details[2],
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

def display_product_details(product_id: str) -> None:
    """
    Display the details of a selected product.
    
    Args:
        product_id (str): Unique identifier of the product.
    """
    product_details = get_product_details(product_id)

    if product_details:
        clear_screen()
        print(f"\n=== Product Details ===")
        print(f"Category: {product_details['category']}")
        print(f"Product Name: {product_details['product_name']}")
        print(f"Description: {product_details['short_description']}")
        print(f"Color: {product_details['colors']}")
        print(f"Price: ₱{product_details['price']}")
        print(f"Stock: {product_details['stock']}")
        
        input("Press Enter to continue...")
    else:
        print("Product not found.")
        input("Press Enter to continue...")