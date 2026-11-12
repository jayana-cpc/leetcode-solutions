class MyHashSet:

    def __init__(self):
        self.hashSet = []

    def add(self, key: int) -> None:
        if key not in self.hashSet:
            self.hashSet.append(key)

    def remove(self, key: int) -> None:
        for i in reversed(range(len(self.hashSet))):
            if self.hashSet[i] == key:
                self.hashSet.pop(i)

    def contains(self, key: int) -> bool:
        return key in self.hashSet
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)