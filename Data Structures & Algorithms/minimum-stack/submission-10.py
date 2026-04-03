class MinStack:

    def __init__(self):
        self.stack = []
        self.minArr = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minArr:
            self.minArr.append(min(val, self.minArr[-1]))
        else:
            self.minArr.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minArr.pop()
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)
        
