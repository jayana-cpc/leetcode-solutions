class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        res = []

        def backtrack(i, cur, total):
            if total == target: 
                res.append(cur[:])
                return
            if i >= n or total > target:
                return
            
            # include nums[i]
            if nums[i] + total <= target:
                cur.append(nums[i])
                backtrack(i, cur, total+nums[i])
                cur.pop()

            # dont include nums[i]
            backtrack(i+1, cur, total)

        backtrack(0, [], 0)
        return res


