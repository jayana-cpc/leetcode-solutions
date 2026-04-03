class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(curr, allowed):
            if len(curr) == len(nums):
                res.append(curr[:])
                return
            if not allowed:
                return
            
            for num in allowed:
                curr.append(num)
                copy = set(allowed)
                copy.remove(num)
                backtrack(curr, copy)
                curr.pop()
        backtrack([], set(nums))
        return res