class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dups = {}

        for i in nums:
            if i in dups.keys():
                return True
            else:
                dups[i] = 1
        return False