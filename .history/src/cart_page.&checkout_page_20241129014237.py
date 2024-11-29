class CheckoutPage:
    def __init__(self):
        self.products = {
            "Laptop": 65000,
            "Headphones": 2500,
            "Smartphone": 35000,
            "Keyboard": 1200,
            "Mouse": 800,
        }
        self.cart = {}

    def display_products(self):
        print("\n📦 Available Products:")
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
            print("❌ Product not found. Please select a valid product.")

    def view_cart(self):
        if not self.cart:
            print("\n🛒 Your cart is empty.")
            return 0
        else:
            print("\n🛒 Your Cart:")
            total_cost = 0
            for product, quantity in self.cart.items():
                cost = self.products[product] * quantity
                total_cost += cost
                print(f"{product}: {quantity} x ₱{self.products[product]:,} = ₱{cost:,}")
            print(f"💵 Subtotal: ₱{total_cost:,}")
            return total_cost

    def apply_discounts(self, total):
        discount = 0
        if total >= 100000:
            discount = total * 0.10  # 10% discount for purchases over ₱100,000
            print(f"🎉 Discount applied: ₱{discount:,} (10% off)")
        elif total >= 50000:
            discount = total * 0.05  # 5% discount for purchases over ₱50,000
            print(f"🎉 Discount applied: ₱{discount:,} (5% off)")
        return discount

    def checkout(self):
        print("\n🔔 Checkout:")
        if not self.cart:
            print("❌ Your cart is empty. Add items before checking out.")
            return

        total_cost = self.view_cart()
        discount = self.apply_discounts(total_cost)
        final_total = total_cost - discount

        print(f"💳 Final Total: ₱{final_total:,}")
        while True:
            confirm = input("Proceed with payment? (yes/no): ").strip().lower()
            if confirm == "yes":
                print("\n✅ Payment successful! Here's your receipt:")
                self.generate_receipt(final_total, discount)
                self.cart.clear()
                break
            elif confirm == "no":
                print("\n❌ Payment canceled. Returning to the main menu.")
                break
            else:
                print("❌ Invalid input. Please type 'yes' or 'no'.")

    def generate_receipt(self, total, discount):
        print("\n🧾 Receipt:")
        print("=" * 30)
        for product, quantity in self.cart.items():
            cost = self.products[product] * quantity
            print(f"{product}: {quantity} x ₱{self.products[product]:,} = ₱{cost:,}")
        print("-" * 30)
        print(f"Subtotal: ₱{self.view_cart():,}")
        print(f"Discount: -₱{discount:,}")
        print(f"Total Paid: ₱{total:,}")
        print("=" * 30)
        print("Thank you for shopping with us! 😊")


def main():
    checkout = CheckoutPage()
    while True:
        print("\n📋 Options:")
        print("1. View Products")
        print("2. Add to Cart")
        print("3. View Cart")
        print("4. Checkout")
        print("5. Exit")
        choice = input("➡️ Choose an option (1-5): ").strip()

        if choice == "1":
            checkout.display_products()
        elif choice == "2":
            checkout.display_products()
            product = input("🛍️ Enter the product name to add: ").strip()
            try:
                quantity = int(input(f"🔢 Enter quantity for {product}: "))
                if quantity > 0:
                    checkout.add_to_cart(product, quantity)
                else:
                    print("❌ Quantity must be greater than 0.")
            except ValueError:
                print("❌ Invalid quantity. Please enter a number.")
        elif choice == "3":
            checkout.view_cart()
        elif choice == "4":
            checkout.checkout()
        elif choice == "5":
            print("👋 Thank you for visiting! Goodbye!")
            break
        else:
            print("❌ Invalid option. Please choose from the menu.")

if __name__ == "__main__":
    main()