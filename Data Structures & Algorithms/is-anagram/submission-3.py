class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        t_hash = {}
        s_hash = {}
        if len(s) != len(t):
            return False
        for i in range(len(t)):
            if s[i] in s_hash.keys():
                s_hash[s[i]] += 1
            if t[i] in t_hash.keys():
                t_hash[t[i]] += 1
            if s[i] not in s_hash.keys():
                s_hash[s[i]] = 1
            if t[i] not in t_hash.keys():
                t_hash[t[i]] = 1
        for i in s:
            if i not in t_hash.keys():
                return False
        for i in t:
            if i not in s_hash.keys():
                return False
        for i in s:
            if s_hash[i] != t_hash[i]:
                return False
        return True