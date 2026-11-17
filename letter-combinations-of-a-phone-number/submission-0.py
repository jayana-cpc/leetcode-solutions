class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        res = []
        def dfs(digits, curr):
            if len(digits) <= 0:
                res.append(''.join(curr[:]))
                return
            
            for letter in mapping[digits[0]]:
                curr.append(letter)
                dfs(digits[1:], curr)
                curr.pop()
        dfs(digits, [])
        return res
