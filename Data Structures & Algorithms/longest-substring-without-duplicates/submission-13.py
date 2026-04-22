class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        longest = 0

        l = 0 

        for r in range(len(s)):
            while window and s[r] in window:
                window.remove(s[l])
                l += 1
            window.add(s[r])
            longest = max(longest, r - l + 1)
        return longest


