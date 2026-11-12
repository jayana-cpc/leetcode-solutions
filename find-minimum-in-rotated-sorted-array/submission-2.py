class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        m = (l + r) // 2
        while l < r:
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
            m = (l + r) // 2
        return nums[m] 