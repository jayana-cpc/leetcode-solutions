class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        def rec(i, j):
            if i == len(s):
                return True
            elif j == len(t):
                return False
            elif s[i] == t[j]:
                return rec(i+1, j+1)
            else:
                return rec(i, j+1)
        return rec(0,0)