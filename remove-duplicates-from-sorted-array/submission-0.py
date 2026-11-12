class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = len(nums) - 1
        while index > 0:
            print(index)
            if nums[index] == nums[index-1]:
                nums.pop(index)
                if index >= len(nums):
                    index -= 1
                
            else:
                index -= 1
        return len(nums)

        