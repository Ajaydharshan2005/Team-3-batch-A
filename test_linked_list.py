import unittest

from inventory import Inventory
from linked_list import LinkedList
from product import Product


class TestLinkedList(unittest.TestCase):
    def test_append_and_traverse(self):
        products = LinkedList()
        products.append("first")
        products.append("second")

        self.assertEqual(list(products), ["first", "second"])
        self.assertEqual(len(products), 2)
        self.assertEqual(products.head.data, "first")
        self.assertEqual(products.tail.data, "second")

    def test_indexing_and_slicing(self):
        products = LinkedList()
        for value in range(4):
            products.append(value)

        self.assertEqual(products[0], 0)
        self.assertEqual(products[-1], 3)
        self.assertEqual(products[1:3], [1, 2])

    def test_empty_list(self):
        products = LinkedList()

        self.assertTrue(products.is_empty())
        self.assertEqual(list(products), [])


class TestInventoryAnalysis(unittest.TestCase):
    def test_inventory_uses_linked_list_and_enumerates_products(self):
        inventory = Inventory()
        inventory.add_product(Product(1, "Pen", 2.0, 3))
        inventory.add_product(Product(2, "Book", 5.0, 4))

        self.assertIsInstance(inventory.products, LinkedList)
        self.assertEqual(
            [(number, product.product_id) for number, product in inventory.enumerate_products()],
            [(1, 1), (2, 2)],
        )
        self.assertEqual(inventory.total_inventory_value(), 26.0)


if __name__ == "__main__":
    unittest.main()