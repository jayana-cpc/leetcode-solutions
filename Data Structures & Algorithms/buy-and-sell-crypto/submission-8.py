class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        def rec(l, r):
            if r == len(prices):
                return 0
            elif prices[r] < prices[l]:
                return rec(r, r)
            else:
                return max((prices[r] - prices[l]), rec(l, r + 1))
        return rec(0, 0)


        # profit = 0
        # l = 0

        # for r in range(len(prices)):
        #     if prices[r] < prices[l]:
        #         l = r
        #     else:
        #         profit = max(profit, prices[r] - prices[l])
        # return profit