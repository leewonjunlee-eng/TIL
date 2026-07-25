from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = float("inf")
        best = 0

        for price in prices:
            if price < low:
                low = price

            if price - low > best:
                best = price - low

        return best
