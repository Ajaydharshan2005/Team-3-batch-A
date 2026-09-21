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


def show_menu():

    print("\n")
    print("=" * 50)
    print("          MINI INVENTORY MANAGER")
    print("=" * 50)

    print("1. Add Product")
    print("2. Display Inventory")
    print("3. Search Product")
    print("4. Update Quantity")
    print("5. Exit")

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

            print(
                "\nThank you for using "
                "Mini Inventory Manager!"
            )

            break

        else:

            print(
                "Invalid choice. "
                "Please select 1-5."
            )


if __name__ == "__main__":
    main()