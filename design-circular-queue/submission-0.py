class MyCircularQueue:
    """
    [2,-1,-1]
    """
    def __init__(self, k: int):
        self.array = [-1] * k 
        self.size = 0
        self.cap = k
        self.rear = 0
        self.front = 0
    def enQueue(self, value: int) -> bool:
        if self.size < self.cap:
            self.array[self.rear] = value
            self.size += 1
            self.rear = self.getIndex(self.rear + 1)
            
            return True
        return False

    def deQueue(self) -> bool:
        if self.size < 1:
            return False
        self.array[self.getIndex(self.front)] = -1
        self.front = self.getIndex(self.front + 1)
        self.size -= 1
        return True
        
    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.array[self.getIndex(self.front)]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.array[self.getIndex(self.rear - 1)]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.cap
    
    def getIndex(self, pos):
        return pos % self.cap


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()