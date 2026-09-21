class InventoryAlgorithms:

    @staticmethod
    def total_inventory_value(products):
        total = 0.0
        for product in products:
            total += product.get_value()
        return total

    @staticmethod
    def sliding_window_max_k_value(products, k):
        n = len(products)

        if n == 0:
            return 0.0, []

        if k <= 0 or k > n:
            return 0.0, []

        values = [p.get_value() for p in products]

        current_sum = sum(values[:k])
        max_sum = current_sum
        max_start = 0

        for i in range(1, n - k + 1):
            current_sum = current_sum - values[i - 1] + values[i + k - 1]
            if current_sum > max_sum:
                max_sum = current_sum
                max_start = i

        max_window = products[max_start:max_start + k]
        return max_sum, max_window

    @staticmethod
    def two_pointers_price_pair(products, target_price):
        if len(products) < 2:
            return None, None

        sorted_products = sorted(products, key=lambda p: p.price)
        prices = [p.price for p in sorted_products]

        left = 0
        right = len(prices) - 1

        while left < right:
            current_sum = prices[left] + prices[right]

            if current_sum == target_price:
                return sorted_products[left], sorted_products[right]
            elif current_sum < target_price:
                left += 1
            else:
                right -= 1

        return None, None
