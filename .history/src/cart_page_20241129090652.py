import os

class AddToCartPage:
    def __init__(self):
        # Product list
        self.products = {
            "Laptop": 65000,
            "Headphones": 2500,
            "Smartphone": 35000,
            "Keyboard": 1200,
            "Mouse": 800,
        }
        # Cart dictionary: product name -> quantity
        self.cart = {}

    def display_products(self):
        """Display the available products with prices."""
        print("\nAvailable Products:")
        for product, price in self.products.items():
            print(f"{product}: ₱{price:,}")

    def add_to_cart(self, product, quantity):
        """Add a product to the cart."""
        if product in self.products:
            if product in self.cart:
                self.cart[product] += quantity
            else:
                self.cart[product] = quantity
            print(f"{quantity} x {product} added to your cart.")
        else:
            print("Product not found. Please select a valid product.")

    def view_cart(self):
        """Display the cart's contents."""
        if not self.cart:
            print("\nYour cart is empty.")
        else:
            print("\nYour Cart:")
            for product, quantity in self.cart.items():
                cost = self.products[product] * quantity
                print(f"{product}: {quantity} x ₱{self.products[product]:,} = ₱{cost:,}")
