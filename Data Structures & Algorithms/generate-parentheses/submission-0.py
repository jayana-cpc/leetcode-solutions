class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(curr, stack, allowed):
            if not allowed["("] and not allowed[")"]:
                strr = "".join(curr)
                res.append(strr)
                return

            # if stack is empty: CANNOT CLOSE
            if not stack:
                if allowed["("]:
                    curr.append("(")
                    all_copy = allowed.copy()
                    stack.append("(")
                    all_copy["("] -= 1
                    backtrack(curr, stack, all_copy)
                    curr.pop()
                    stack.pop()
                else:
                    return
            else:
                if allowed["("]:
                    curr.append("(")
                    all_copy = allowed.copy()
                    stack.append("(")
                    all_copy["("] -= 1
                    backtrack(curr, stack, all_copy)
                    curr.pop()
                    stack.pop()
                if allowed[")"]:
                    curr.append(")")
                    all_copy = allowed.copy()
                    stack_copy = stack.copy()
                    stack_copy.pop()
                    all_copy[")"] -= 1
                    backtrack(curr, stack_copy, all_copy)
                    curr.pop()
        backtrack([], [], {"(": n, ")": n})
        return res






