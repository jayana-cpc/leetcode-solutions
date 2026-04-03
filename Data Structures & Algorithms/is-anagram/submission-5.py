class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        shash = [0]*26
        thash = [0]*26
        for i in s:
            shash[ord(i) - ord('a')] += 1
        for i in t:
            thash[ord(i) - ord('a')] += 1
        
        return shash == thash