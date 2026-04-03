class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        closes = {")":"(", "}": "{", "]":"["}
        stack = []
        for i in s:
            if i in closes and len(stack) > 0:
                if stack[-1] == closes[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        if len(stack) == 0:
            return True
        else:
            return False


