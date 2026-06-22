class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def rec(i, bought):
            if i == len(prices):
                return 0
            if (i, bought) in memo:
                return memo[(i, bought)]
            if bought:
                sell = prices[i] + rec(i+1, False)
                hold = rec(i+1, bought)
                memo[(i, bought)] =  max(sell, hold)
                return memo[(i, bought)]
            else:
                buy = -prices[i] + rec(i+1, True)
                skip = rec(i+1, bought)
                memo[(i, bought)] = max(buy, skip)
                return memo[(i, bought)]
        return rec(0, False)
            