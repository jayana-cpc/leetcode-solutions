class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += word + "big juicy cock"
        return res
    def decode(self, s: str) -> List[str]:
        res = s.split("big juicy cock") 
        return res[:-1]

