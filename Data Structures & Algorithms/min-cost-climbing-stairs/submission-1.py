class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        cache = [-1]*(n+1)
        
        def dfs(x):
            if x >= n:
                return 0
            if cache[x] != -1:
                return cache[x]
            cache[x] = cost[x] + min(dfs(x+1), dfs(x+2))
            return cache[x]
          
        return min(dfs(0), dfs(1))
