class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        new = s
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            elif s[l] != s[r]:
                new1 = s[0:l] + s[l+1:]
                new2 =  s[0:r] + s[r+1:]
                return new1 == new1[::-1] or new2 == new2[::-1]
 
        return True

        