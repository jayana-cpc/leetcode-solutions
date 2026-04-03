class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        thang = {}

        for i in range(len(nums)):
            if (target - nums[i]) in thang.keys():
                return [thang.get(target - nums[i]), i]
            thang[nums[i]] = i
        