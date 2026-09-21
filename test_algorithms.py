import unittest
from product import Product
from algorithms import InventoryAlgorithms
from inventory import Inventory


class TestTotalInventoryValue(unittest.TestCase):

    def test_empty_inventory(self):
        products = []
        result = InventoryAlgorithms.total_inventory_value(products)
        self.assertEqual(result, 0.0)

    def test_single_product(self):
        products = [Product(101, "Pen", 20.0, 50)]
        result = InventoryAlgorithms.total_inventory_value(products)
        self.assertEqual(result, 1000.0)

    def test_multiple_products(self):
        products = [
            Product(101, "Pen", 20.0, 50),
            Product(102, "Book", 100.0, 20),
            Product(103, "Bag", 800.0, 10),
            Product(104, "Bottle", 300.0, 15),
        ]
        result = InventoryAlgorithms.total_inventory_value(products)
        self.assertEqual(result, 1000.0 + 2000.0 + 8000.0 + 4500.0)

    def test_zero_quantity(self):
        products = [
            Product(101, "Pen", 20.0, 0),
            Product(102, "Book", 100.0, 0),
        ]
        result = InventoryAlgorithms.total_inventory_value(products)
        self.assertEqual(result, 0.0)

    def test_zero_price(self):
        products = [
            Product(101, "Free", 0.0, 100),
        ]
        result = InventoryAlgorithms.total_inventory_value(products)
        self.assertEqual(result, 0.0)


class TestSlidingWindowMaxKValue(unittest.TestCase):

    def setUp(self):
        self.sample_products = [
            Product(101, "Pen", 20.0, 50),
            Product(102, "Book", 100.0, 20),
            Product(103, "Bag", 800.0, 10),
            Product(104, "Bottle", 300.0, 15),
            Product(105, "Notebook", 50.0, 40),
        ]

    def test_empty_inventory(self):
        max_sum, window = InventoryAlgorithms.sliding_window_max_k_value([], 2)
        self.assertEqual(max_sum, 0.0)
        self.assertEqual(window, [])

    def test_k_zero(self):
        max_sum, window = InventoryAlgorithms.sliding_window_max_k_value(self.sample_products, 0)
        self.assertEqual(max_sum, 0.0)
        self.assertEqual(window, [])

    def test_k_negative(self):
        max_sum, window = InventoryAlgorithms.sliding_window_max_k_value(self.sample_products, -1)
        self.assertEqual(max_sum, 0.0)
        self.assertEqual(window, [])

    def test_k_larger_than_n(self):
        max_sum, window = InventoryAlgorithms.sliding_window_max_k_value(self.sample_products, 10)
        self.assertEqual(max_sum, 0.0)
        self.assertEqual(window, [])

    def test_k_equals_one(self):
        max_sum, window = InventoryAlgorithms.sliding_window_max_k_value(self.sample_products, 1)
        self.assertEqual(max_sum, 8000.0)
        self.assertEqual(len(window), 1)
        self.assertEqual(window[0].product_id, 103)

    def test_k_equals_n(self):
        max_sum, window = InventoryAlgorithms.sliding_window_max_k_value(self.sample_products, 5)
        self.assertEqual(len(window), 5)
        expected_sum = 1000.0 + 2000.0 + 8000.0 + 4500.0 + 2000.0
        self.assertEqual(max_sum, expected_sum)

    def test_k_equals_two_basic(self):
        max_sum, window = InventoryAlgorithms.sliding_window_max_k_value(self.sample_products, 2)
        expected_sums = [
            1000.0 + 2000.0,
            2000.0 + 8000.0,
            8000.0 + 4500.0,
            4500.0 + 2000.0,
        ]
        self.assertEqual(max_sum, 8000.0 + 4500.0)
        self.assertEqual(len(window), 2)

    def test_k_equals_three(self):
        max_sum, window = InventoryAlgorithms.sliding_window_max_k_value(self.sample_products, 3)
        expected_sums = [
            1000.0 + 2000.0 + 8000.0,
            2000.0 + 8000.0 + 4500.0,
            8000.0 + 4500.0 + 2000.0,
        ]
        self.assertEqual(max_sum, 2000.0 + 8000.0 + 4500.0)
        self.assertEqual(len(window), 3)

    def test_single_product_window(self):
        products = [Product(101, "Only", 50.0, 5)]
        max_sum, window = InventoryAlgorithms.sliding_window_max_k_value(products, 1)
        self.assertEqual(max_sum, 250.0)
        self.assertEqual(len(window), 1)
        self.assertEqual(window[0].product_id, 101)

    def test_window_products_correct_ids(self):
        products = [
            Product(1, "A", 10.0, 1),
            Product(2, "B", 20.0, 1),
            Product(3, "C", 30.0, 1),
            Product(4, "D", 40.0, 1),
            Product(5, "E", 50.0, 1),
        ]
        max_sum, window = InventoryAlgorithms.sliding_window_max_k_value(products, 3)
        self.assertEqual(max_sum, 30.0 + 40.0 + 50.0)
        self.assertEqual(window[0].product_id, 3)
        self.assertEqual(window[1].product_id, 4)
        self.assertEqual(window[2].product_id, 5)


class TestTwoPointersPricePair(unittest.TestCase):

    def setUp(self):
        self.sample_products = [
            Product(101, "Pen", 20.0, 50),
            Product(102, "Book", 100.0, 20),
            Product(103, "Bag", 800.0, 10),
            Product(104, "Bottle", 300.0, 15),
            Product(105, "Notebook", 50.0, 40),
        ]

    def test_less_than_two_products(self):
        p1, p2 = InventoryAlgorithms.two_pointers_price_pair([], 100)
        self.assertIsNone(p1)
        self.assertIsNone(p2)

        p1, p2 = InventoryAlgorithms.two_pointers_price_pair([self.sample_products[0]], 100)
        self.assertIsNone(p1)
        self.assertIsNone(p2)

    def test_pair_exists_exact(self):
        p1, p2 = InventoryAlgorithms.two_pointers_price_pair(self.sample_products, 120.0)
        self.assertIsNotNone(p1)
        self.assertIsNotNone(p2)
        self.assertAlmostEqual(p1.price + p2.price, 120.0)

    def test_pair_exists_pen_and_bottle(self):
        p1, p2 = InventoryAlgorithms.two_pointers_price_pair(self.sample_products, 320.0)
        self.assertIsNotNone(p1)
        self.assertIsNotNone(p2)
        self.assertAlmostEqual(p1.price + p2.price, 320.0)

    def test_pair_exists_book_and_bottle(self):
        p1, p2 = InventoryAlgorithms.two_pointers_price_pair(self.sample_products, 400.0)
        self.assertIsNotNone(p1)
        self.assertIsNotNone(p2)
        self.assertAlmostEqual(p1.price + p2.price, 400.0)

    def test_no_pair_exists_too_small(self):
        p1, p2 = InventoryAlgorithms.two_pointers_price_pair(self.sample_products, 10.0)
        self.assertIsNone(p1)
        self.assertIsNone(p2)

    def test_no_pair_exists_too_large(self):
        p1, p2 = InventoryAlgorithms.two_pointers_price_pair(self.sample_products, 5000.0)
        self.assertIsNone(p1)
        self.assertIsNone(p2)

    def test_no_pair_exists_in_between(self):
        p1, p2 = InventoryAlgorithms.two_pointers_price_pair(self.sample_products, 999.0)
        self.assertIsNone(p1)
        self.assertIsNone(p2)

    def test_pair_with_zero_price(self):
        products = [
            Product(1, "Free", 0.0, 10),
            Product(2, "Cheap", 50.0, 5),
            Product(3, "Expensive", 100.0, 2),
        ]
        p1, p2 = InventoryAlgorithms.two_pointers_price_pair(products, 50.0)
        self.assertIsNotNone(p1)
        self.assertIsNotNone(p2)
        self.assertAlmostEqual(p1.price + p2.price, 50.0)

    def test_duplicate_prices(self):
        products = [
            Product(1, "A", 10.0, 1),
            Product(2, "B", 10.0, 1),
            Product(3, "C", 30.0, 1),
        ]
        p1, p2 = InventoryAlgorithms.two_pointers_price_pair(products, 20.0)
        self.assertIsNotNone(p1)
        self.assertIsNotNone(p2)
        self.assertAlmostEqual(p1.price + p2.price, 20.0)

    def test_pair_at_extremes(self):
        products = [
            Product(1, "Min", 5.0, 1),
            Product(2, "Mid1", 15.0, 1),
            Product(3, "Mid2", 25.0, 1),
            Product(4, "Max", 95.0, 1),
        ]
        p1, p2 = InventoryAlgorithms.two_pointers_price_pair(products, 100.0)
        self.assertIsNotNone(p1)
        self.assertIsNotNone(p2)
        self.assertAlmostEqual(p1.price + p2.price, 100.0)

    def test_target_negative(self):
        p1, p2 = InventoryAlgorithms.two_pointers_price_pair(self.sample_products, -50.0)
        self.assertIsNone(p1)
        self.assertIsNone(p2)


class TestInventoryIntegration(unittest.TestCase):

    def setUp(self):
        self.inventory = Inventory()
        self.inventory.add_product(Product(101, "Pen", 20.0, 50))
        self.inventory.add_product(Product(102, "Book", 100.0, 20))
        self.inventory.add_product(Product(103, "Bag", 800.0, 10))
        self.inventory.add_product(Product(104, "Bottle", 300.0, 15))
        self.inventory.add_product(Product(105, "Notebook", 50.0, 40))

    def test_total_inventory_value_integration(self):
        total = self.inventory.total_inventory_value()
        expected = 1000.0 + 2000.0 + 8000.0 + 4500.0 + 2000.0
        self.assertEqual(total, expected)

    def test_max_k_product_value_integration(self):
        max_sum, window = self.inventory.max_k_product_value(3)
        expected_sum = 2000.0 + 8000.0 + 4500.0
        self.assertEqual(max_sum, expected_sum)
        self.assertEqual(len(window), 3)

    def test_product_pair_search_integration_exists(self):
        p1, p2 = self.inventory.product_pair_search(120.0)
        self.assertIsNotNone(p1)
        self.assertIsNotNone(p2)
        self.assertAlmostEqual(p1.price + p2.price, 120.0)

    def test_product_pair_search_integration_not_found(self):
        p1, p2 = self.inventory.product_pair_search(9999.0)
        self.assertIsNone(p1)
        self.assertIsNone(p2)


class TestComplexityVerification(unittest.TestCase):

    def test_sliding_window_linear(self):
        sizes = [10, 50, 100, 500]
        for n in sizes:
            products = [Product(i, f"P{i}", float(i), 1) for i in range(n)]
            k = n // 4 if n >= 4 else 1
            max_sum, window = InventoryAlgorithms.sliding_window_max_k_value(products, k)
            self.assertEqual(len(window), k)
            self.assertGreater(max_sum, 0)

    def test_two_pointers_linear_search(self):
        n = 200
        products = [Product(i, f"P{i}", float(i * 2 + 1), 1) for i in range(n)]
        target = products[5].price + products[n - 3].price
        p1, p2 = InventoryAlgorithms.two_pointers_price_pair(products, target)
        self.assertIsNotNone(p1)
        self.assertIsNotNone(p2)
        self.assertAlmostEqual(p1.price + p2.price, target)


if __name__ == "__main__":
    unittest.main()
