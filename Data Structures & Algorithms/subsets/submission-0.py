class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res, sol = [], []

        def backtrack(i):
            if i == n:
                res.append(sol[:])
                return
            
            # dont use nums[i]
            backtrack(i+1)

            # lets try out nums[i]
            sol.append(nums[i])
            backtrack(i+1)
            # ok we're back
            sol.pop()
        backtrack(0)
        return res