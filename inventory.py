from product import Product
from algorithms import InventoryAlgorithms


class Inventory:

    def __init__(self):
        self.products = []

    # Add Product
    def add_product(self, product):
        # Check duplicate ID
        if self.search_by_id(product.product_id) is not None:
            print("Product ID already exists.")
            return False

        # Validate price
        if product.price < 0:
            print("Price cannot be negative.")
            return False

        # Validate quantity
        if product.quantity < 0:
            print("Quantity cannot be negative.")
            return False

        self.products.append(product)

        print("Product added successfully.")
        return True

    # Display Inventory
    def display_inventory(self):

        if len(self.products) == 0:
            print("\nInventory is empty.")
            return

        print("\n" + "=" * 60)
        print("                    INVENTORY")
        print("=" * 60)

        print(
            f"{'ID':<10}"
            f"{'Name':<15}"
            f"{'Price':<12}"
            f"{'Quantity':<10}"
            f"{'Value':<12}"
        )

        print("-" * 60)

        for product in self.products:
            product.display()

        print("=" * 60)

    # Search by Product ID
    def search_by_id(self, product_id):

        for product in self.products:
            if product.product_id == product_id:
                return product

        return None

    # Search by Product Name
    def search_by_name(self, name):

        for product in self.products:
            if product.name.lower() == name.lower():
                return product

        return None

    # Search by ID or Name
    def search_product(self, search_value):

        # Try searching by ID
        try:
            product_id = int(search_value)

            product = self.search_by_id(product_id)

            if product is not None:
                return product

        except ValueError:
            pass

        # Search by name
        return self.search_by_name(search_value)

    # Update Quantity
    def update_quantity(self, product_id, new_quantity):

        product = self.search_by_id(product_id)

        if product is None:
            print("Product not found.")
            return False

        if new_quantity < 0:
            print("Quantity cannot be negative.")
            return False

        product.quantity = new_quantity

        print("Quantity updated successfully.")
        return True

    def total_inventory_value(self):
        return InventoryAlgorithms.total_inventory_value(self.products)

    def max_k_product_value(self, k):
        return InventoryAlgorithms.sliding_window_max_k_value(self.products, k)

    def product_pair_search(self, target_price):
        return InventoryAlgorithms.two_pointers_price_pair(self.products, target_price)