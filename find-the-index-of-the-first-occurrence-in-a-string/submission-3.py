class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        curr = ""
        r = 0
        for l in range(len(haystack)):
            while r < len(haystack) and r - l + 1 <= len(needle):
                curr += haystack[r]
                r += 1
            if curr == needle:
                return l
            curr = curr[1:]
        return -1