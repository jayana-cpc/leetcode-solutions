class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        cache = [-1]*len(nums)

        def dfs(x, nums):
            if x >= len(nums):
                return 0
            elif cache[x] == -1:
                skip = dfs(x+1, nums)
                rob = nums[x] + dfs(x+2, nums)

                cache[x] = max(skip, rob)
            return cache[x]

        cache = [-1]*len(nums)
        first = dfs(0, nums[:-1])
        cache = [-1]*len(nums)
        last = dfs(0, nums[1:])
        return max(first, last)
        
        