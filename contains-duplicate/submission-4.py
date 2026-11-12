class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        list = set()
        for x in nums:
            if x in list:
                return True
            list.add(x)
        return False