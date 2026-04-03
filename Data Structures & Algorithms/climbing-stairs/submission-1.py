class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        def helper(n):
            if -1 < n < 3:
                return n
            if n not in cache:
                cache[n] = helper(n-1) + helper(n-2)
            return cache[n]
        return helper(n)
        