class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for op in operations: 
            if op == "C":
                stack.pop()
            elif op == "D":
                stack.append(int(stack[-1]) * 2)
            elif op == "+":
                last = stack.pop()
                secondToLast = stack.pop()
                final = secondToLast + last
                stack.append(secondToLast)
                stack.append(last)
                stack.append(final)
            else:
                stack.append(int(op))
        
        return sum(stack)