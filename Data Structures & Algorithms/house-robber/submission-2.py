class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        cache = [-1] * (n + 1)

        def dfs(x):
            if x >= n:
                return 0
            if cache[x] != -1:
                return cache[x]
            cache[x] = max(nums[x] + dfs(x+2), dfs(x+1))
            return cache[x]
        best = 0
        for i in range(n):
            best = max(best, dfs(i))
        return best