class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: 
            return 0
        if len(nums) == 1: 
            return 1
        n = set(nums)
        best = 1
        for i in nums:
            if i - 1 not in n:
                curr = 1
                num = i
                while num + 1 in n:
                    curr += 1
                    if curr > best:
                        best = curr
                    num += 1
        return best

        