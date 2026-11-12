class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        longest = 0
        window = set()
        curr = 0

        while r < len(s):
            if s[r] in window:
                window.remove(s[l])
                l += 1
                curr = len(window)
            elif s[r] not in window:
                window.add(s[r])
                curr += 1
                longest = max(longest, curr)
                r += 1
        return longest

        