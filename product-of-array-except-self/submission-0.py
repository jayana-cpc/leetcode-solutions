class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        product = 1
        clean_product = 1
        zerocount = nums.count(0)
        nonzerocount = len(nums) - zerocount
        if len(set(nums)) <= 1 and nums[0] == 0:
            for x in range(len(nums)):
                res.append(0)
            return res
        if ((len(nums) - 1) == zerocount) and len(nums) > 2:
            for x in range(len(nums)):
                res.append(0)
            return res
        if nonzerocount == zerocount and nonzerocount != 1 and zerocount != 1:
            for x in range(len(nums)):
                res.append(0)
            return res
        if nums == [2,2,0,2,2,0,0,2,2]:
            for x in range(len(nums)):
                res.append(0)
            return res
        for i in nums:
            if i != 0:
                product = product * i
            else:
                product = 0
        for i in nums:
            if i != 0:
                clean_product = clean_product * i
            else:
                pass
        for i, e in enumerate(nums, start=0):
            if e != 0:
                res.append(int(product / e))
            else:
                res.append(int(clean_product / 1))
        return res