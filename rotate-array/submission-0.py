class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k > len(nums):
            k = k % len(nums)
            
        index = len(nums) - k
        j = 0
        while index < len(nums):
            temp = nums[index]
            nums.pop(index)
            nums.insert(j, temp)
            index+=1
            j+=1

        