class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        found = False
        l = 0
        s = 0
        res = 10000000
        for r in range(len(nums)):
            s += nums[r]   

            while s >= target:
                found = True
                res = min(res, r - l + 1)
                s -= nums[l]
                l += 1

        if found: return res
        else: return 0