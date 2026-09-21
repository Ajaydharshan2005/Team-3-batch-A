from product import Product
from inventory import Inventory


def add_product(inventory):

    try:
        product_id = int(input("Enter Product ID: "))

        name = input("Enter Product Name: ").strip()

        if name == "":
            print("Product name cannot be empty.")
            return

        price = float(input("Enter Price: "))

        quantity = int(input("Enter Quantity: "))

        if price < 0:
            print("Price cannot be negative.")
            return

        if quantity < 0:
            print("Quantity cannot be negative.")
            return

        product = Product(
            product_id,
            name,
            price,
            quantity
        )

        inventory.add_product(product)

    except ValueError:
        print("Invalid input. Please enter valid values.")


def search_product(inventory):

    if len(inventory.products) == 0:
        print("Inventory is empty.")
        return

    search_value = input(
        "Enter Product ID or Product Name: "
    ).strip()

    product = inventory.search_product(search_value)

    if product is None:
        print("Product not found.")
    else:
        print("\nProduct Found:")
        print("-" * 60)

        print(
            f"{'ID':<10}"
            f"{'Name':<15}"
            f"{'Price':<12}"
            f"{'Quantity':<10}"
            f"{'Value':<12}"
        )

        print("-" * 60)

        product.display()


def update_quantity(inventory):

    try:
        product_id = int(
            input("Enter Product ID: ")
        )

        new_quantity = int(
            input("Enter New Quantity: ")
        )

        inventory.update_quantity(
            product_id,
            new_quantity
        )

    except ValueError:
        print("Invalid input.")


def show_total_value(inventory):
    total = inventory.total_inventory_value()
    print(f"\nTotal Inventory Value: {total:.2f}")


def show_max_k_product_value(inventory):

    if len(inventory.products) == 0:
        print("Inventory is empty.")
        return

    try:
        k = int(input("Enter the value of k (consecutive products): "))

        if k <= 0:
            print("k must be a positive integer.")
            return

        if k > len(inventory.products):
            print(f"k cannot be larger than the number of products ({len(inventory.products)}).")
            return

        max_sum, window_products = inventory.max_k_product_value(k)

        print(f"\nMaximum total value of {k} consecutive products: {max_sum:.2f}")
        print("Products in window:")
        print("-" * 60)
        print(
            f"{'ID':<10}"
            f"{'Name':<15}"
            f"{'Price':<12}"
            f"{'Quantity':<10}"
            f"{'Value':<12}"
        )
        print("-" * 60)
        for product in window_products:
            product.display()

    except ValueError:
        print("Invalid input. Please enter a valid integer for k.")


def show_product_pair_search(inventory):

    if len(inventory.products) < 2:
        print("At least 2 products are required for pair search.")
        return

    try:
        target_price = float(input("Enter target price sum: "))

        if target_price < 0:
            print("Target price cannot be negative.")
            return

        p1, p2 = inventory.product_pair_search(target_price)

        if p1 is None or p2 is None:
            print(f"\nNo product pair found with price sum of {target_price:.2f}.")
        else:
            print(f"\nProduct pair found with price sum of {target_price:.2f}:")
            print("-" * 60)
            print(
                f"{'ID':<10}"
                f"{'Name':<15}"
                f"{'Price':<12}"
                f"{'Quantity':<10}"
                f"{'Value':<12}"
            )
            print("-" * 60)
            p1.display()
            p2.display()
            print(f"\nSum of prices: {p1.price:.2f} + {p2.price:.2f} = {p1.price + p2.price:.2f}")

    except ValueError:
        print("Invalid input. Please enter a valid number for target price.")


def show_menu():

    print("\n")
    print("=" * 50)
    print("          MINI INVENTORY MANAGER")
    print("=" * 50)

    print("1. Add Product")
    print("2. Display Inventory")
    print("3. Search Product")
    print("4. Update Quantity")
    print("5. Total Inventory Value")
    print("6. Maximum K-Product Value")
    print("7. Product Pair Search")
    print("8. Exit")

    print("=" * 50)


def main():

    inventory = Inventory()

    while True:

        show_menu()

        choice = input(
            "Enter your choice: "
        ).strip()

        if choice == "1":

            add_product(inventory)

        elif choice == "2":

            inventory.display_inventory()

        elif choice == "3":

            search_product(inventory)

        elif choice == "4":

            update_quantity(inventory)

        elif choice == "5":

            show_total_value(inventory)

        elif choice == "6":

            show_max_k_product_value(inventory)

        elif choice == "7":

            show_product_pair_search(inventory)

        elif choice == "8":

            print(
                "\nThank you for using "
                "Mini Inventory Manager!"
            )

            break

        else:

            print(
                "Invalid choice. "
                "Please select 1-8."
            )


if __name__ == "__main__":
    main()