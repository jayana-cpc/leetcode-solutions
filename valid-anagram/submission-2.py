class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        slist = list(s.strip(""))
        tlist = list(t.strip(""))

        sdict = {}
        tdict = {} 
        for x in range(len(s)):
            sdict[s[x]] = 1 + sdict.get(s[x], 0)
        for x in range(len(t)):
            tdict[t[x]] = 1 + tdict.get(t[x], 0)
        if sdict == tdict:
            return True
        else:
            return False

