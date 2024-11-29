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
    print("\nAvailable Products:")
    for product, price in self.products.items():
        print(f"{product}: ₱{price:,}")

def add_to_cart(self, product, quantity):
    if product in self.products:
        if product in self.cart:
                self.cart[product] += quantity
        else:
                self.cart[product] = quantity
        print(f"{quantity} x {product} added to your cart.")
    else:
            print("Product not found. Please select a valid product.")

def view_cart(self):
    if not self.cart:
            print("\nYour cart is empty.")
    else:
        print("\nYour Cart:")
        for product, quantity in self.cart.items():
            cost = self.products[product] * quantity
            print(f"{product}: {quantity} x ₱{self.products[product]:,} = ₱{cost:,}")

# Execution
cart_page = AddToCartPage()

while True:
    print("\nOptions:")
    print("1. View Products")
    print("2. Add to Cart")
    print("3. View Cart")
    print("4. Save and Exit")
    choice = input("Choose an option (1-4): ").strip()

    if choice == "1":
        cart_page.display_products()
    elif choice == "2":
        cart_page.display_products()
        product = input("Enter the product name to add: ").strip()
        try:
            quantity = int(input(f"Enter quantity for {product}: "))
            if quantity > 0:
                cart_page.add_to_cart(product, quantity)
            else:
                print("Quantity must be greater than 0.")
        except ValueError:
            print("Invalid quantity. Please enter a number.")
    elif choice == "3":
        cart_page.view_cart()
    elif choice == "4":
        print("\nSaving your cart. You can now proceed to checkout.")
        with open("cart_data.txt", "w") as file:
            for product, quantity in cart_page.cart.items():
                file.write(f"{product},{quantity}\n")
        break
    else:
        print("Invalid option. Please choose from the menu.")