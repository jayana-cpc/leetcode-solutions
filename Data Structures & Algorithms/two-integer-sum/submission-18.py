class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compliments = {}

        for i in range(len(nums)):
            if target - nums[i] in compliments.keys():
                return[compliments[target - nums[i]], i]
            else:
                compliments[nums[i]] = i


        