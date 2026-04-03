class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(char for char in s if char.isalnum())
        a = 0
        b = len(s) - 1

        while b > a:
            if s[a].lower() != s[b].lower(): return False
            else: 
                a+=1
                b-=1
        return True 
        