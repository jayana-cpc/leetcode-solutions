class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        lenn = 100000
        l = 0
        total = 0
        found = False
        for r in range(len(nums)):
            total += nums[r]
            
            while total >= target:
                found = True
                lenn = min(lenn, r - l + 1)
                total -= nums[l]
                l += 1

        if not found:
            return 0
        return lenn
            
            