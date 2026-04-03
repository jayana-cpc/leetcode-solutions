class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hm = {}

        for i in nums:
            if i in hm.keys():
                return True
            else:
                hm[i] = 1
        return False