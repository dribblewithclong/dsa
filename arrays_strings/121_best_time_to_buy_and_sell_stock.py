class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n_min = 0
        price_min = prices[0]
        n_max = len(prices) - 1
        price_max = prices[n_max]
        arr_diff = []

        for i in range(1, len(prices)):
            n_tmp = i
            price_tmp = prices[i]

            if price_tmp < price_min and n_tmp < n_max:
                price_min = price_tmp
                n_min = n_tmp
            if price_tmp > price_max and n_tmp > n_min:
                price_max = price_tmp
                n_max = n_tmp
            if price_tmp < price_min and price_tmp < price_max:
                if price_max > price_min:
                    arr_diff.append(price_max - price_min)
                price_min = price_tmp
                price_max = price_tmp
                n_min = n_tmp
                n_max = n_tmp

        if price_max > price_min:
            arr_diff.append(price_max - price_min)

        if len(arr_diff) == 0:
            return 0

        price_output = arr_diff[0]
        for i in range(1, len(arr_diff)):
            if arr_diff[i] > price_output:
                price_output = arr_diff[i]

        return price_output
