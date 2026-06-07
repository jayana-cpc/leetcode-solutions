class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ""
        l, r = 0, len(s) - 1
        best = 1
        res = ""
        for i in range(len(s)):
            l, r = i, i 
            while l > -1 and r < len(s) and s[l] == s[r]:
                if r - l + 1 >= best:
                    res = s[l:r+1]
                    best = r - l + 1
                l -= 1
                r += 1
            l, r = i, i + 1 
            while l > -1 and r < len(s) and s[l] == s[r]:
                if r - l + 1 >= best:
                    res = s[l:r+1]
                    best = r - l + 1
                l -= 1
                r += 1

        return res
