class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [-1] * (n + 1)

        def dfs(x):
            if x == n:
                return 1
            if x > n:
                return 0
            if cache[x] != -1:
                return cache[x]
            
            cache[x] = dfs(x+1) + dfs(x+2)

            return cache[x]
        return dfs(0)