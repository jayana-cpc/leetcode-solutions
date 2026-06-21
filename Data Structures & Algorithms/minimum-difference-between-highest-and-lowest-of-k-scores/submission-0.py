class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        [1, 2, 3, 3, 5, 6]
        low = float("inf")
        l = 0
        for r in range(k-1, len(nums)):
            low = min(low, nums[r] - nums[l])
            l += 1
        return low
            
