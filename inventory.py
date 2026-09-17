from product import Product


class Inventory:

    def __init__(self):
        self.products = []

    # 1. Add Product
    def add_product(self, product):
        # Check duplicate ID
        if self.search_by_id(product.product_id) is not None:
            print("Product ID already exists.")
            return False

        self.products.append(product)

        print("Product added successfully.")
        return True

    # 2. Display Inventory
    def display_inventory(self):

        if len(self.products) == 0:
            print("Inventory is empty.")
            return

        print(
            f"{'ID':<10}"
            f"{'Name':<15}"
            f"{'Price':<10}"
            f"{'Quantity':<10}"
        )

        print("-" * 45)

        for product in self.products:
            product.display()

    # 3. Search by ID
    def search_by_id(self, product_id):

        for product in self.products:
            if product.product_id == product_id:
                return product

        return None

    # 4. Search by Name
    def search_by_name(self, name):

        for product in self.products:
            if product.name.lower() == name.lower():
                return product

        return None

    # 5. Update Quantity
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