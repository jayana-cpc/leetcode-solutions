class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = [-1]*len(nums)

        def dfs(x):
            if x >= len(nums):
                return 0
            elif cache[x] == -1:
                skip = dfs(x+1)
                rob = nums[x] + dfs(x+2)

                cache[x] = max(skip, rob)
            return cache[x]
        return dfs(0)
