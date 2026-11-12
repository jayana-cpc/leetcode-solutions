class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1
        # for i in range(len(haystack) - len(needle)):
        #     if str[i]