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
        print(pivot)
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










        # if nums[m] == target:
        #     return m
        # while l < r:
        #     if nums[m] == target:
        #         return m
        #     elif nums[l] == target:
        #         return l
        #     elif nums[r] == target:
        #         return r
        #     elif nums[m] > nums[r] and target <= nums[r]:
        #         l = m + 1
        #     elif nums[m] > nums[r] and target > nums[r]:
        #         r = m
        #     elif nums[m] < nums[r] and target < nums[r]:
        #         r = m
        #     elif nums[m] < nums[r] and target >= nums[r] and nums[l] < target:
        #         l = m + 1
        #     elif nums[m] < nums[r] and target >= nums[r] and nums[l] >= target:
        #         r = m
        #     m = (l+r) // 2
        # if nums[m] == target:
        #     return m    
        # return -1
