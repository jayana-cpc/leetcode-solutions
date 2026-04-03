class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zerocount = 0
        for i in nums:
            if i == 0: zerocount += 1
        if zerocount > 1: return [0] * len(nums)
        product = 1
        zproduct = 1
        for i in nums:
            if i == 0: pass
            else: zproduct *= i
            product *= i
            
        
        res = []

        for i in nums:
            if i != 0: res.append(product//i)
            if i == 0: res.append(zproduct)
        return res
            
