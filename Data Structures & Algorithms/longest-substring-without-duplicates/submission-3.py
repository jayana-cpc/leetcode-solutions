class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        best = 0
        l = 0
        count = set()
        for r in range(len(s)):
            while s[r] in count:
                count.remove(s[l])
                l += 1
            if s[r] not in count:
                count.add(s[r])
                
            
            best = max(best, len(count))
        return best