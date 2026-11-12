class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        best = nums[0]

        for num in nums:
            if abs(best) > abs(num):
                best = num
        if best<0 and abs(best) in nums:
            return abs(best)
        return best

            
