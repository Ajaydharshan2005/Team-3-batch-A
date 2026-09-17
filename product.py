class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_value(self):
        return self.price * self.quantity

    def display(self):
        print(
            f"{self.product_id:<10}"
            f"{self.name:<15}"
            f"{self.price:<10.2f}"
            f"{self.quantity:<10}"
        )