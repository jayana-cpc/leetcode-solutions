class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(l, r):
            best = ""
            while l > -1 and r < len(s) and s[l] == s[r]:
                best = s[l:r+1]
                l -= 1
                r += 1
            return best
        odd = ""
        for i in range(len(s)):
            odd = max(expand(i,i), odd, key=len)
        even = ""
        for i in range(len(s) - 1):
            even = max(expand(i, i+1), even, key=len)
        
        return max(even, odd, key=len)