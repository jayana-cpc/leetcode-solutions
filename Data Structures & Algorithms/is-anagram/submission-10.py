class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hm = {}
        t_hm = {}
        for i in range(len(s)):
            s_hm[s[i]] = 1 + s_hm.get(s[i], 0)
        for i in range(len(t)):
            t_hm[t[i]] = 1 + t_hm.get(t[i], 0)
        return s_hm == t_hm 