class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = [-1] * (len(nums) + 1)

        def dfs(x):
            if x >= len(nums):
                return 0
            if cache[x] != -1:
                return cache[x]
            
            # skip house x
            skip = dfs(x+1)
            
            # rob house x
            rob = nums[x] + dfs(x+2)

            cache[x] = max(skip, rob)
            return cache[x]
        
        return dfs(0)
            
            