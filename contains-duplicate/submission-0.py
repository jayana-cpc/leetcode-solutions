class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        a = len(nums)
        b = len(set(nums))
        if a == b:
            return False
        elif a != b:
            return True