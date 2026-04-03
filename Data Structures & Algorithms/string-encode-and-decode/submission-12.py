class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += word + "qwer"
        return res
    def decode(self, s: str) -> List[str]:
        res = s.split("qwer") 
        return res[:-1]

