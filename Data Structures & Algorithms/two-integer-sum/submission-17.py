class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comps = {}

        for i in range(len(nums)):
            if(target - nums[i]) in comps.keys():
                return[comps.get(target - nums[i]), i]
            comps[nums[i]] = i       
            
        