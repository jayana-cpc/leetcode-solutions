class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            res += i
            res += "1nvur799j3bfycvg387574737gdb"
        return res
    def decode(self, s: str) -> List[str]:
        temp = s.split("1nvur799j3bfycvg387574737gdb")
        return temp[:len(temp) - 1]
