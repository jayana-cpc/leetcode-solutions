import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv  
        }
        stack = []
        for i in range(len(tokens)):
            if tokens[i].lstrip('-').isnumeric():
                stack.append(int(tokens[i]))
            else:
                if tokens[i] == '/':
                    temp = int(ops[tokens[i]](stack[-2], stack[-1]))
                else:
                    temp = ops[tokens[i]](stack[-2], stack[-1])
                stack.pop()
                stack.pop()
                stack.append(temp)
        return(stack[-1])