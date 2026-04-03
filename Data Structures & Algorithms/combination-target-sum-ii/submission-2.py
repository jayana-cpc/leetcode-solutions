class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)
        candidates.sort()
        def backtrack(i, curr, total):
            if total == target:
                res.append(curr[:])
                return
            if i >= n or total > target:
                return
            
            # use candidates[i]
            curr.append(candidates[i])
            backtrack(i+1, curr, total+candidates[i])
            curr.pop()
            # dont use  candidates[i] but skip dupes
            while i+1 < n and candidates[i] == candidates[i+1]:
                i += 1
            backtrack(i+1, curr, total)
        backtrack(0, [], 0)
        return res
