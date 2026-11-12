class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack == needle:
            return 0
        if needle not in haystack:
            return -1
        for i in range(len(haystack)):
            temp = ""
            for j in range(len(needle)):
                if haystack[i+j] != needle[j]:
                    break
                else:
                    temp += haystack[i+j]
            if temp == needle:
                return i
        return -1

                

        # if needle in haystack:
        #     return haystack.index(needle)
        # else:
        #     return -1