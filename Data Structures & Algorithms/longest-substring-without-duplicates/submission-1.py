class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        l = 0
        r = l + 1
        best = 1
        curr = 1
        while r < len(s):
            if s[r] not in s[l:r]:
                curr += 1
                if curr > best:
                    best = curr
                r += 1
            else:
                curr = 1
                l += 1
                r = l + 1
        return best