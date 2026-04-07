class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0
        window = set()
        best = 1
        l = 0

        for r in range(len(s)):
            while window and s[r] in window:
                window.remove(s[l])
                l += 1
            window.add(s[r])
            best = max(len(window), best)
        return best
        