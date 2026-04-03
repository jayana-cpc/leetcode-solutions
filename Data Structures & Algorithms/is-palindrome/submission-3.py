class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = ""
        for i in s:
            if i.isalnum():
                temp += i.lower()
        s = temp
        left = 0
        right = len(s) - 1
        
        while left <= right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False
            
        return True
        