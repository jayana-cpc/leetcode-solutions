class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_chars = [0]*26
        t_chars = [0]*26

        for i in range(len(s)):
            s_chars[ord(s[i]) - ord('a')] += 1
            t_chars[ord(t[i]) - ord('a')] += 1
        return s_chars == t_chars