class MyHashSet:

    def __init__(self):
        self.cap = 100
        self.map = [None] * self.cap

    def add(self, key: int) -> None:
        h = hash(key)
        i = h % self.cap

        if self.map[i] is None:
            self.map[i] = [key]
        else:
            if key not in self.map[i]:
                self.map[i].append(key)

    def remove(self, key: int) -> None:
        h = hash(key)
        i = h % self.cap

        if self.map[i] is not None and key in self.map[i]:
            self.map[i].remove(key)

    def contains(self, key: int) -> bool:
        h = hash(key)
        i = h % self.cap

        if self.map[i] is not None and key in self.map[i]:
            return True
        return False
        
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)