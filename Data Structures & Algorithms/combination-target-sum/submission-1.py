class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, sol = [], []
        n = len(nums)

        def backtrack(i, total):
            if total == target:
                res.append(sol[:])
                return
            if i == n or total > target:
                return
            
            # dont use nums[i]
            backtrack(i+1, total)

            # use nums[i]
            sol.append(nums[i])
            backtrack(i, total + nums[i])
            sol.pop()
            # use nums[i] and repear


            
        backtrack(0, 0)
        return res


            