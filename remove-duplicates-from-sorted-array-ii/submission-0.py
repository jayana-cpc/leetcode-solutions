class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        hm = {}
        i = 0   
        while i < len(nums):
            if nums[i] in hm.keys():
                if hm[nums[i]] < 2:
                    hm[nums[i]] += 1
                    i += 1
                else:
                    nums.pop(i)

            else:
                hm[nums[i]] = 1
                i += 1
        return len(nums)
                