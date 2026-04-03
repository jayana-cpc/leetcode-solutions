class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0: return False
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        for c in s:
            if c in closeToOpen:
                if stack and closeToOpen[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
                
            else:
                stack.append(c)
        if stack: return False
        return True

        