class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        if nums[0] <= nums[-1]:
            return nums[0]

        while l <= r:
            m = (l + r) // 2
            if (nums[m] < nums[m-1] and nums[m] < nums[m+1]):
                return nums[m]
            elif (nums[m] > nums[m-1] and nums[m] > nums[m+1]):
                return nums[m+1]
            elif nums[m] < nums[l] and nums[m] < nums[r]:
                r = m - 1
            elif nums[m] > nums[l] and nums[m] > nums[r]:
                l = m + 1
        return nums[m]    