class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}

        for i in range(len(nums)):
            diff = target - nums[i] #2
            if diff in hm:
                return [hm[diff], i]
            else:
                hm[target - diff] = i