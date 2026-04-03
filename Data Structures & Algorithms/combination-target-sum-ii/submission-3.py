class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        
        def backtrack(i, curr, total):
            if total == target:
                res.append(curr[:])
                return
            if i >= len(candidates) or total > target:
                return

            
           
            # I want to use candidates[i]
            curr.append(candidates[i])
            backtrack(i+1, curr, total+candidates[i])
            curr.pop()

            # I dont want to use candidates[i]
            while i + 1 < len(candidates) and candidates[i+1] == candidates[i]:
                i+= 1
            backtrack(i+1, curr, total)
        backtrack(0, [], 0)
        return res





