#!/usr/bin/env python3
from typing import List


class Solution:
    """
    From a given array need to find the max profit a buyer can achieved.

    Methods:
        maxProfit(prices): Take a list of integer and find the max profit.
    """

    def maxProfit(self, prices: List[int]) -> int:
        """
        Take a price list and return the max profit that a user can get.

        Params:
            :dtype prices: A list of integer.
            :rtype: An integer.
        """
        min_value = prices[0]
        max_profit = 0
        left = 0
        right = len(prices)

        while left < right:
            if prices[left] > min_value:
                max_profit = max(prices[left] - min_value, max_profit)

            if prices[left] < min_value:
                min_value = prices[left]
            left += 1

        return max_profit


def test_case():
    """
    This is to varify the correctness of solution.maxProfit methods.
    """

    test_cases = [
        ([7, 1, 5, 3, 6, 4], 5),  # Test Case 1
        ([7, 6, 4, 3, 1], 0),  # Test Case 2
        ([2, 4, 1], 2),  # Test Case 3
    ]

    solution = Solution()
    for _, (prices, expected) in enumerate(test_cases):
        result = solution.maxProfit(prices)
        assert result == expected, f"Erro: {prices=}, {expected}, but got {result}"
    print(f"Congrats! All {len(test_cases)} test cases passed.")


if __name__ == "__main__":
    test_case()
