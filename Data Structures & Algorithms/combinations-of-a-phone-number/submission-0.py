class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hm = {
            2: ["A", "B", "C"],
            3: ["D", "E", "F"],
            4: ["G", "H", "I"],
            5: ["J", "K", "L"],
            6: ["M", "N", "O"],
            7: ["P", "Q", "R", "S"],
            8: ["T", "U", "V"],
            9: ["W", "X", "Y", "Z"],
        }
        res = []
        def add(curr, digi):
            if not digi:
                new = "".join(curr)
                if new:
                    res.append(new)
                return
            
            num = int(digi[0]) # 4
            chars = hm[num] # ["G", "H", "I"]
            for char in chars:
                curr.append(char.lower())
                add(curr, digi[1:])
                curr.pop()
        add([], digits)
        return res




