class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS = [0]*26
        countT = [0]*26

        for char in s:
            countS[ord(char) - ord('a')] = countS[ord(char) - ord('a')] + 1
        for char in t:
            countT[ord(char) - ord('a')] = countT[ord(char) - ord('a')] + 1
        return countS == countT
        