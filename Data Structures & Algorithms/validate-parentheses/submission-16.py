class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hm = {"}": "{", ")":"(", "]":"["}

        for char in s:
            if char not in hm:
                stack.append(char)
            else:
                if not stack or stack.pop() != hm[char]:
                    return False
        return not stack
