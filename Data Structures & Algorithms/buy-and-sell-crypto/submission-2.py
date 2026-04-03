class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 1
        best = 0
        while sell < len(prices):
            profit = prices[sell] - prices[buy]
            best = max(profit, best)
            if profit < 0:
                buy = sell
                sell = buy + 1
            else:
                sell += 1
        return best