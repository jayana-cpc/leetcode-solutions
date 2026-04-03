class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # detect first collision
        f = 0
        s = 0

        while True:
            s = nums[s]
            f = nums[nums[f]]
            if s == f:
                break
        s2 = 0

        while True:
            if s == s2:
                return s
            s = nums[s]
            s2 = nums[s2]
        
