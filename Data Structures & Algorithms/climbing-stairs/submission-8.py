class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [-1]*n

        def dfs(x):
            if x > n:
                return 0
            elif x == n:
                return 1
            elif cache[x] == -1:
                cache[x] = dfs(x+1) + dfs(x+2)
            return cache[x]
        return dfs(0)