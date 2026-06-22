class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[-1, -1] for _ in range(len(prices) + 1)]
        dp[len(prices)][0] = 0
        dp[len(prices)][1] = 0
        # 0 -> buy, 1 -> sell

        for i in range(len(prices) - 1, -1, -1):
            dp[i][1] = max(prices[i] + dp[i+1][0], dp[i+1][1])
            dp[i][0] = max(-prices[i] + dp[i+1][1], dp[i+1][0])
        return dp[0][0]
        # old memo solution
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
        return rec(0, 0)
            