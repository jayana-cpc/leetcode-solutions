class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        cache = [[-1]*len(t) for _ in range(len(s))]
        
        def rec(i, j):
            if i == len(s):
                return True
            elif j == len(t):
                return False
            elif cache[i][j] != -1:
                return cache[i][j]
            elif s[i] == t[j]:
                cache[i][j] = rec(i+1, j+1)
                return cache[i][j]
            else:
                cache[i][j] =  rec(i, j+1)
                return cache[i][j]
        return rec(0,0)