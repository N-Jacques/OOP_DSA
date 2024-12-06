import os
import sqlite3
from typing import Dict, Optional
from src.productDetails_page import display_product_details

db_path = "./database/data.db"

def clear_screen() -> None:
    """Clear the console screen across different operating systems."""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_products(category: Optional[str] = None) -> Dict[str, Dict]:
    """
    Fetch products and their colors, stock, and price from the database.
    
    Args:
        category (str, optional): Filter products by category. Defaults to None.
    
    Returns:
        Dict of products with their details and variants.
    """
    try:
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            
            # Prepare the SQL query based on whether a category is specified
            if category:
                cursor.execute("""
                    SELECT p.product_id, p.product_name, p.description, pc.color, pc.price, pc.stock
                    FROM product p
                    JOIN product_color pc ON p.product_id = pc.product_id
                    WHERE p.category = ?
                """, (category,))
            else:
                cursor.execute("""
                    SELECT p.product_id, p.product_name, p.description, pc.color, pc.price, pc.stock
                    FROM product p
                    JOIN product_color pc ON p.product_id = pc.product_id
                """)
            
            # Organize products into a structured dictionary
            products = {}
            for row in cursor.fetchall():
                product_id = row[0]
                if product_id not in products:
                    products[product_id] = {
                        "product_name": row[1],
                        "description": row[2],
                        "variants": []
                    }
                products[product_id]["variants"].append({
                    "color": row[3],
                    "price": row[4],
                    "stock": row[5]
                })
            
            return products
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return {}
    except Exception as e:
        print(f"Unexpected error: {e}")
        return {}

def display_products(category: Optional[str] = None) -> Dict[str, Dict]:
    """
    Display products, optionally filtered by category.
    
    Args:
        category (str, optional): Filter products by category. Defaults to None.
    
    Returns:
        Dict of displayed products.
    """
    clear_screen()
    products = get_products(category)
    
    if not products:
        print(f"No products found in the {category if category else 'database'}")
        input("Press Enter to continue...")
        return {}

    print(f"\n=== Products in {category if category else 'All Categories'} ===")
    print(f"{'No.':<10}{'Product Name':<25}{'Color':<20}{'Price':<10}{'Stock':<10}")
    print("-" * 70)
    
    product_number = 1  # Start numbering from 1
    product_map = {}  # To map the numbers to product IDs
    
    for pid, details in products.items():
        for variant in details["variants"]:
            print(f"{product_number:<10}{details['product_name']:<25}{variant['color']:<20}₱{variant['price']:<10}{variant['stock']:<10}")
            product_map[product_number] = pid  # Map the number to the product_id
            product_number += 1
    
    return product_map  # Return the mapping of number to product ID

def product_selection(filtered_products: Dict[int, str]) -> Optional[str]:
    """
    Allow the user to select a product by sequential number.
    
    Args:
        filtered_products (Dict): Dictionary mapping numbers to product IDs.
    
    Returns:
        Selected product ID or None.
    """
    while True:
        try:
            product_number = input("Enter the product number to view details (or 0 to go back): ").strip()
            
            if product_number == "0":
                return None
            
            product_number = int(product_number)
            if product_number in filtered_products:
                return filtered_products[product_number]
            
            print("Invalid selection. Please try again.")
        
        except KeyboardInterrupt:
            print("\nOperation cancelled.")
            return None
        except ValueError:
            print("Please enter a valid number.")

def products_page(category: Optional[str] = None) -> None:
    """
    Main function to display products and handle product selection.
    
    Args:
        category (str, optional): Filter products by category. Defaults to None.
    """
    filtered_products = display_products(category)

    if filtered_products:
        product_id = product_selection(filtered_products)

        if product_id:
            display_product_details(product_id)
