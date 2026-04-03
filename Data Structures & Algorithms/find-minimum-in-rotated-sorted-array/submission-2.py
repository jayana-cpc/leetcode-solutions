class Solution:
    def findMin(self, nums: List[int]) -> int:
        # [6, 1, 2, 3, 4, 5]
        #        m
        l = 0
        r = len(nums) - 1

        while l < r:
            m = (l + r) // 2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        return nums[l]
