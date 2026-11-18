class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        n = len(nums)
        insert = 1
        for i in range(1, len(nums)):
            if nums[i-1] != nums[i]:
                nums[insert] = nums[i]
                insert += 1
        return insert
        

