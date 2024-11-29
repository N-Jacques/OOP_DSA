# purchaseProduct.py
from src.productsDetails import products

def purchase_product(product_id, quantity):
    if product_id not in products:
        return "Invalid product ID"
    
    product = products[product_id]
    if product["stock"] < quantity:
        return "Insufficient stock"
    
    total_price = product["price"] * quantity
    products[product_id]["stock"] -= quantity
    return f"Purchase successful!\nTotal: ₱{total_price:.2f}"