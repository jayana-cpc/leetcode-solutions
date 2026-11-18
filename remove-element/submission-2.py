class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        # [3,2,2,3]
        # []
        r = len(nums) - 1
        l = 0
        while r > -1 and nums[r] == val:
            r -= 1
        while l <= r:
            if nums[l] == val:
                nums[l], nums[r] = nums[r], nums[l]
            l += 1
            while r > -1 and nums[r] == val:
                r -= 1
        return l

                

