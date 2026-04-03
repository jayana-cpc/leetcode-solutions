class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            res += i
            res += "no fuckin way thisll be an item in strs"
        return res
    def decode(self, s: str) -> List[str]:
        temp = s.split("no fuckin way thisll be an item in strs")
        return temp[:len(temp) - 1]
