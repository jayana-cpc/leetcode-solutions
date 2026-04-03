class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        r = 0
        profit = 0

        for l in range(0, len(prices) - 1):
            r = l + 1
            while r < len(prices):
               profit = max(profit, prices[r] - prices[l])
               r += 1
            
        return profit
        