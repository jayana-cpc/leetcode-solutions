class Solution:
    def myAtoi(self, s: str) -> int:
        limit = 2**31
        i = 0
        while i < len(s) and s[i] == " ":
            i += 1

        s = s[i:]
        if not s:
            return 0
        sign = -1 if s[0] == "-" else 1

        if s[0] in "+-":
            s = s[1:]
        
        res = 0
        zero_ascii = ord('0')
        for char in s:
            if '0' <= char <= '9':
                
                res = (res*10) + (ord(char) - zero_ascii)
                if res >= limit:
                    return -limit if sign == -1 else limit - 1
            else:
                break
        return res * sign
