class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res = res + str(len(word)) + "#" + word
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        # 5#Hello5#World
        while i < len(s):
            length = ""
            while s[i].isnumeric():
                length = length + s[i]
                i += 1
            i += 1
            word = ""
            for _ in range(int(length)):
                word = word + s[i]
                i += 1
            res.append(word)
        return res

            




