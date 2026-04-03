class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dups = []

        for i in nums:
            if i in dups:
                return True
            else:
                dups.append(i)
        return False
         