class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupes = {}
        for i in nums:
            if dupes.get(i, 0) != 0:
                return True
            else:
                dupes[i] = 1
        return False
        

         