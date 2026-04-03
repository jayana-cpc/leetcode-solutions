class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        m = (l+r) // 2
        pivot = 0
        
        while l < r:
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
            m = (l+r) // 2
        
        pivot = m

        r = len(nums) - 1
        l = 0
        if target >= nums[pivot] and target <= nums[r]:
            l = pivot
        else:
            r = pivot

        while l <= r:
            m = (l+r) // 2

            if nums[m] > target:
                r = m -1
            elif nums[m] < target:
                l = m + 1
            elif nums[m] == target:
                return m
        return -1    