class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        def rec(i, j):
            if i == len(s):
                return True
            elif j == len(s):
                return False
            elif (i, j) in memo:
                return memo[(i, j)]
            elif s[i:j+1] in wordDict:
                memo[(i, j)] = rec(j+1, j+1) or rec(i, j+1)
                return memo[(i, j)]
            else:
                memo[(i, j)] = rec(i, j+1)
                return memo[(i, j)]
        return rec(0, 0)