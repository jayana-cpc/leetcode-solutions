class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        if nums[-1] >= nums[0]:
            return nums[0]
        while l <= r:
            m = (l + r) // 2
            if nums[m + 1] < nums[m]:
                return nums[m + 1]
            elif nums[m] > nums[r]:
                l = m + 1
            elif nums[m] < nums[r]:
                r = m
        return m