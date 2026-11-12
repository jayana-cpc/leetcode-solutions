class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        nums = list(set(nums))
        nums.sort()
        count = 0
        longest = 0
        [2, 3, 4, 5, 10, 20]
        for i in range(len(nums) - 1):
            if nums[i+1] == nums[i] + 1:
                count+=1
                if count > longest:
                    longest = count
            else: 
                count = 0
        return longest + 1   

        