class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return max(nums)

        def dfs(x, nums):
            if x >= len(nums):
                return 0
            if cache[x] != -1:
                return cache[x]
            
            # skip house x
            skip = dfs(x+1, nums)
            
            # rob house x
            rob = nums[x] + dfs(x+2, nums)

            cache[x] = max(skip, rob)
            return cache[x]

        # dont rob first
        cache = [-1] * (len(nums) + 1)
        skip_first = dfs(0, nums[1:])
        cache = [-1] * (len(nums) + 1)
        skip_last = dfs(0, nums[:-1])
        return max(skip_first, skip_last)

        