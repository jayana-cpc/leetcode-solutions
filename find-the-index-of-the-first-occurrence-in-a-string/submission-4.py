class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l = 0
        for r in range(len(needle), len(haystack) + 1):
            if haystack[l:r] == needle:
                return l
            l += 1
        return -1