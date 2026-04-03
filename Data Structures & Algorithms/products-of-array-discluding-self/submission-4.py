class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        
        for i in range(1, len(nums)):
            res[i] = res[i - 1] * nums[i - 1]
        
        suf = 1

        for i in reversed(range(len(nums) - 1)):
            suf *= nums[i+1]
            res[i] = res[i] * suf

        return res
