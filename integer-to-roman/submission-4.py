class Solution:
    def intToRoman(self, num: int) -> str:
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
        res = ""
        for value, symbol in reversed(value_symbol.items()):
            count = num // value
            res += symbol * count
            num %= value
        return res
            
