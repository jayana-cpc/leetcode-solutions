class Solution:
    def isValid(self, s: str) -> bool:
        openToClose = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }
        stack = []

        for char in s:
            if char not in openToClose:
                stack.append(char)
            else:
                p = openToClose[char] 
                if not stack or p != stack.pop():
                    return False
        return len(stack) == 0


