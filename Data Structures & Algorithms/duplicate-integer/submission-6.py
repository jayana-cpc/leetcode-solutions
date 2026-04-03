class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupes = {}
        for i in nums:
            if i in dupes.keys():
                return True
            else:
                dupes[i] = 1
        return False
         