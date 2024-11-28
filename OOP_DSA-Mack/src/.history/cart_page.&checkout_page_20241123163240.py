def __init__(self):
        self.products = {
            "Laptop": 65000,
            "Headphones": 2500,
            "Smartphone": 35000,
            "Keyboard": 1200,
            "Mouse": 800
        }
        self.cart = {}

def display_products(self):
        print("\nAvailable Products:")
        for product, price in self.products.items():
            print(f"{product}: ₱{price:,}")

def add_to_cart(self, product, quantity):
        if product in self.products:
            if product in self.cart:
                self.cart[product] += quantity
            else:
                self.cart[product] = quantity
            print(f"✅ {quantity} x {product} added to your cart.")
        else:
            print("❌ Product not found. Please select from the available products.")

def remove_from_cart(self, product):
        if product in self.cart:
            del self.cart[product]
            print(f"✅ {product} removed from your cart.")
        else:
            print("❌ Product not found in your cart.")

def view_cart(self):
        if not self.cart:
            print("\n🛒 Your cart is empty.")
        else:
            print("\n🛒 Your Shopping Cart:")
            total_cost = 0
            for product, quantity in self.cart.items():
                cost = self.products[product] * quantity
                total_cost += cost
                print(f"{product}: {quantity} x ₱{self.products[product]:,} = ₱{cost:,}")
            print(f"💵 Total: ₱{total_cost:,}")

def checkout(self):
        if not self.cart:
            print("❌ Your cart is empty. Add items before checking out.")
        else:
            print("\n✅ Checkout Summary:")
            self.view_cart()
            print("\nThank you for shopping with us! 😊")
            self.cart.clear()


def main():
    cart = ShoppingCart()
    while True:
        print("\n📋 Options:")
        print("1. View Products")
        print("2. Add to Cart")
        print("3. Remove from Cart")
        print("4. View Cart")
        print("5. Checkout")
        print("6. Exit")
        choice = input("➡️ Choose an option (1-6): ").strip()

        if choice == "1":
            cart.display_products()
        elif choice == "2":
            cart.display_products()
            product = input("🛍️ Enter the product name to add: ").strip()
            try:
                quantity = int(input(f"🔢 Enter quantity for {product}: "))
                if quantity > 0:
                    cart.add_to_cart(product, quantity)
                else:
                    print("❌ Quantity must be greater than 0.")
            except ValueError:
                print("❌ Invalid quantity. Please enter a number.")
        elif choice == "3":
            product = input("🗑️ Enter the product name to remove: ").strip()
            cart.remove_from_cart(product)
        elif choice == "4":
            cart.view_cart()
        elif choice == "5":
            cart.checkout()
            break
        elif choice == "6":
            print("👋 Thank you for visiting! Goodbye!")
            break
        else:
            print("❌ Invalid option. Please select from the menu.")

'__name__' == '__main__'
main()