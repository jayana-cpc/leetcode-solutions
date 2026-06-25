class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [-1] * (n + 1)
        
        def rec(i):
            if i == n:
                return 1
            elif i > n:
                return 0
            elif memo[i] != -1:
                return memo[i]
            else:
                memo[i] = rec(i+1) + rec(i+2)
                return memo[i]
        return rec(0)