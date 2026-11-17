class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        def dfs(curr, left, right):
            if left == n and right == n:
                res.append(''.join(curr))
                return
            elif left > n or right > n:
                # invalid
                return
            
            if left < n:
                curr.append("(")
                dfs(curr, left+1, right)
                curr.pop()
            if right < left:
                curr.append(")")
                dfs(curr, left, right+1)
                curr.pop()
        dfs([],0,0)
        return res
