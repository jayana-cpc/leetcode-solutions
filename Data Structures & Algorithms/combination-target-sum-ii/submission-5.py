class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # counts = {}
        # for num in candidates:
        #     counts[num] = counts.get(num, 0) + 1
        res, sol = [], []
        n = len(candidates)
        candidates.sort()

        def backtrack(i, total):
            if total == target:
                res.append(sol[:])
                return 
            if total > target or i >= n:
                return


            # dont use candidates[i]
            

            # use candidates[i]
            # counts[candidates[i]] -= 1
            sol.append(candidates[i])
            backtrack(i+1, candidates[i] + total)
            sol.pop()

            while i + 1 < len(candidates) and candidates[i+1] == candidates[i]:
                i+= 1
            backtrack(i+1, total)
        backtrack(0, 0)
        return res