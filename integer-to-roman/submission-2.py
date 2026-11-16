class Solution:
    def __init__(self):
        self.cache = {}
    def lsd_nonzero(self, num):
        string_num = str(num)
        lsd = ""
        for i in range(len(string_num)-1, -1, -1):
            lsd += string_num[i]
            if string_num[i] != "0":
                break
        return int(lsd[::-1])
    
    def intToRoman(self, num: int) -> str:
        if num <= 0:
            return ""
        value_symbol = {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M"
        }
        lsd = self.lsd_nonzero(num)
        if lsd in self.cache:
            return self.cache[lsd]
        og_lsd = lsd
        # if lsd not in (4, 9):
        res = ""
        for value, symbol in reversed(value_symbol.items()):
            while value <= lsd:
                res += symbol
                lsd -= value
        self.cache[og_lsd] = self.intToRoman(num - og_lsd) + res
        return self.cache[og_lsd]
            
