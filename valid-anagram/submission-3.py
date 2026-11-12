class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sHash = {}
        tHash = {}
        for i in s:
            if i in sHash:
                sHash[i] += 1
            else:
                sHash[i] = 1
        for i in t:
            if i in tHash:
                tHash[i] += 1
            else:
                tHash[i] = 1
        if sHash == tHash:
            return True
        else:
            return False
