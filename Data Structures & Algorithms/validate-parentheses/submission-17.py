class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hm = {
            "]":"[",
            ")":"(",
            "}":"{",
        }

        for char in s:
            if char not in hm:
                stack.append(char)
            elif not stack or stack[-1] != hm[char]:
                return False
            else:
                stack.pop()
        return not stack
