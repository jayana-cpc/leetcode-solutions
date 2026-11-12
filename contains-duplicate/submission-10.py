class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dupes = set()
        for i in nums:
            if i in dupes:
                return True
            else:
                dupes.add(i)
        return False