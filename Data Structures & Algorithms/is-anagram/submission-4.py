class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        sm = {}
        tm = {}
        for i in range(len(s)):
            sm[s[i]] = sm.get(s[i], 0) + 1
            tm[t[i]] = tm.get(t[i], 0) + 1
            
        return sm == tm
