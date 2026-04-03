class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        shash = {}
        thash = {}
        for e in t:
            if e in thash: thash[e] += 1
            else: thash[e] = 1
        for i in s:
            if i in shash: shash[i] += 1
            else: shash[i] = 1
            
        return shash == thash

        