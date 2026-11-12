class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hm = {
            ")" : "(",
            "}" : "{",
            "]" : "["
            }
        
        for p in s:
            if p in hm:
                if stack:
                    if stack[-1] == hm[p]:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
            else:
                stack.append(p)
        
        return len(stack) == 0