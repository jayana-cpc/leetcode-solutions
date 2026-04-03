class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr = set()
        best = 0
        l = 0
        for r in range(len(s)):
            while s[r] in curr:
                curr.remove(s[l])
                l+=1
            curr.add(s[r])
            best = max(best, r - l + 1)
        return best
            