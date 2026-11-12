class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for op in operations:
            print(stack)
            if op.lstrip('-').isnumeric():
                stack.append(int(op))
            elif op == "C":
                stack.pop()
            elif op == "D":
                stack.append(int(stack[-1]) * 2)
            elif op == "+":
                stack.append(stack[-1] + stack[-2])
        
        return sum(stack)