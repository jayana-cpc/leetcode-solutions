class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(sol, used):
            if len(sol) >= n*2:
                res.append(sol)
                return
            else:
                if used["("] < n:
                    used["("] += 1
                    temp = sol
                    sol = sol + "("
                    backtrack(sol, used)
                    used["("] -= 1
                    sol = temp
                if used[")"] < used["("]:
                    used[")"] += 1
                    temp = sol
                    sol = sol + ")"
                    backtrack(sol, used)
                    used[")"] -= 1
                    sol = temp
        backtrack("", {"(":0, ")": 0})
        return res
