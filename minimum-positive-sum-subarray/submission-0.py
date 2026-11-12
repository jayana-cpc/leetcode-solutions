class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        
        res = 1000000

        for x in range(l, r+1):
            left = 0
            s = sum(nums[:x])
            if s > 0:
                res = min(res, s)
            for right in range(x,len(nums)):
                s += nums[right]
                s -= nums[left]
                if s > 0:
                    res = min(res, s)
                left += 1
        if res == 1000000:
            return -1
        else:
            return res
    