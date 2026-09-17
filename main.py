from product import Product
from inventory import Inventory


def main():

    inventory = Inventory()

    # Add products
    inventory.add_product(
        Product(101, "Pen", 20, 50)
    )

    inventory.add_product(
        Product(102, "Book", 100, 20)
    )

    inventory.add_product(
        Product(103, "Bag", 800, 10)
    )

    inventory.add_product(
        Product(104, "Bottle", 300, 15)
    )

    # Display
    print("\n--- INVENTORY ---")
    inventory.display_inventory()

    # Search by ID
    print("\n--- SEARCH BY ID ---")

    product = inventory.search_by_id(103)

    if product:
        product.display()
    else:
        print("Product not found.")

    # Search by name
    print("\n--- SEARCH BY NAME ---")

    product = inventory.search_by_name("Book")

    if product:
        product.display()
    else:
        print("Product not found.")

    # Update quantity
    print("\n--- UPDATE QUANTITY ---")

    inventory.update_quantity(103, 15)

    print("\n--- UPDATED INVENTORY ---")
    inventory.display_inventory()


if __name__ == "__main__":
    main()