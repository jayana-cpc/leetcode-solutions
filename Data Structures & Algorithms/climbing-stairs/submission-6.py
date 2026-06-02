class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [0]*(n+1)
        print(cache)

        def dfs(x):
            if x == 0:
                return 1
            if x < 0:
                return 0
            if cache[x]:
                return cache[x]
            cache[x] = dfs(x-1) + dfs(x-2)
            return cache[x] 
        return dfs(n)
