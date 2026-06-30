class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()


        def backtrack(i, total, used):
            if total == target:
                res.append(used[:])
                return
            elif i == len(candidates) or total > target:
                return
            else:
                # use i
                used.append(candidates[i])
                backtrack(i + 1, total + candidates[i], used)
                used.pop()
                # skip i (ensure next i != prev_i)
                while i + 1 < len(candidates) and candidates[i+1] == candidates[i]:
                    i += 1
                backtrack(i+1, total, used)
        backtrack(0, 0, [])
        return res