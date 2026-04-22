class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        window = {}
        l = 0
        maxF = 0
        res = 0

        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1
            maxF = max(maxF, window[s[r]])

            while (r - l + 1) - maxF > k:
                window[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res

