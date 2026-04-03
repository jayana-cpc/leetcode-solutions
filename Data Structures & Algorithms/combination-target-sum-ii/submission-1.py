class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()
        n = len(candidates)
        candidates.sort()
        def backtrack(i, curr, total):
            if total == target:
                res.add(tuple(curr))
                return
            if i >= n or total > target:
                return
            
            # use candidates[i]
            curr.append(candidates[i])
            backtrack(i+1, curr, total+candidates[i])
            curr.pop()
            # dont use  candidates[i]
            backtrack(i+1, curr, total)
        backtrack(0, [], 0)
        return [list(combination) for combination in res]
