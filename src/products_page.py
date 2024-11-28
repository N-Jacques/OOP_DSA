# productlistCategory.py
from productsDetails import products
from category_page import categories


def view_by_category(category):
    print(f"\nProducts in {category}:")
    print(f"{'ID':<10}{'Name':<15}{'Price':<10}{'Stock':<10}")
    print("-" * 45)
    for pid, product in products.items():
        if product["category"] == category:
            print(f"{pid:<10}{product['name']:<15}₱{product['price']:<10.2f}{product['stock']:<10}")

def view_all_products():
    print("\nAll Products:")
    print(f"{'ID':<10}{'Name':<15}{'Price':<10}{'Stock':<10}{'Category':<15}")
    print("-" * 60)
    for pid, product in products.items():
        print(f"{pid:<10}{product['name']:<15}₱{product['price']:<10.2f}{product['stock']:<10}{product['category']:<15}")

def display_menu():
    print("\n=== Product Viewer ===")
    print("1. View All Products")
    print("2. View by Category")
    print("3. Purchase Product")
    print("4. Exit")

def show_categories():
    print("\nCategories:")
    for i, category in enumerate(categories, 1):
        print(f"{i}. {category}")

def main():
    while True:
        display_menu()
        choice = input("Enter choice (1-4): ")
        
        if choice == "1":
            view_all_products()
        elif choice == "2":
            show_categories()
            cat_choice = int(input("Select category (1-5): ")) - 1
            if 0 <= cat_choice < len(categories):
                view_by_category(categories[cat_choice])
        elif choice == "3":
            pid = input("Enter product ID: ")
            qty = int(input("Enter quantity: "))
            print(purchase_product(pid, qty))
        elif choice == "4":
            print("Thank you for using Product Viewer!")
            break

if __name__ == "__main__":
    from purchaseProduct import purchase_product
    main()