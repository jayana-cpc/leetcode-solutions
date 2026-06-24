class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        memo = {}
        def rec(i, prev):
            if i == len(nums):
                return 0
            elif (i, prev) in memo:
                return memo[(i, prev)]
            skip = rec(i+1, prev)
            use = 0
            if nums[i] > prev:
                use = 1 + rec(i+1, nums[i])
            memo[(i, prev)] = max(use, skip)
            return memo[(i, prev)]
        return rec(0, float("-inf"))
            