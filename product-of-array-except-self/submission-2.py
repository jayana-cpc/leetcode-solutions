class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroCount = 0
        total = None
        totalZero = None
        if nums[0] == 0: 
            zeroCount+=1
            total = nums[0]
            totalZero = 1
        else: 
            totalZero = nums[0]
            total = nums[0]
        result = []
        for i in nums[1:]:
            if i != 0: 
                total *= i
                totalZero *= i
            else:
                total *= i
                zeroCount += 1
        for i in nums:
            if i == 0 and zeroCount == 1: result.append(totalZero)
            elif i == 0 and zeroCount > 1: result.append(0)
            else: result.append(total // i)
        return result
        