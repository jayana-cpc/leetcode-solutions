class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        def dfs(i):
            if i == len(s):
                return 1
            if s[i] == "0":
                return 0
            if i in memo:
                return memo[i]
            memo[i] = dfs(i+1)
            if i + 1 < len(s) and int(s[i:i+2]) <= 26:
                memo[i] += dfs(i+2)
            return memo[i]
        return dfs(0)