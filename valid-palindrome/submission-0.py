class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = ""
        for letter in s:
            if letter.isalpha() or letter.isnumeric():
                l += letter
            else:
                pass
        string = l.lower()
        revstring = string[::-1]
        if string == revstring:
            return True
        else:
            return False