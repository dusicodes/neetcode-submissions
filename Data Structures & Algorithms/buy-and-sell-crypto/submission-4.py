class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i ,j, m = 0, 0, 0

        while i < len(prices):
            j = i + 1
            while j < len(prices) and prices[i] < prices[j]:
                m = max(m, prices[j] - prices[i])
                j += 1
            i += 1
        return m





