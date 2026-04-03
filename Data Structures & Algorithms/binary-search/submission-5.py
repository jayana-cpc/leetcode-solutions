class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0 # 3
        r = len(nums) - 1 # 5 
        m = (l + r) // 2 # 4
        while nums[m] != target and l <= r:
            if nums[m] > target:
                r = m - 1
                m = (l + r) // 2 
            else: 
                l = m + 1
                m = (l + r) // 2
               
        if nums[m] == target:
            return m
        else:
            return -1
        