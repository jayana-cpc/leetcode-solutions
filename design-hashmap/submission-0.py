class MyHashMap:

    def __init__(self):
        self.cap = 10000
        self.map = [None] * self.cap

    def put(self, key: int, value: int) -> None:
        h = hash(key)
        i = h % self.cap

        if self.map[i] is None:
            self.map[i] = [[key, value]]
        else:
            for item in self.map[i]:
                if item[0] == key:
                    item[1] = value
                    return
            self.map[i].append([key, value])

    def get(self, key: int) -> int:
        h = hash(key)
        i = h % self.cap

        if self.map[i] is None:
            return -1
        else:
            for item in self.map[i]:
                if item[0] == key:
                    return item[1]
            return -1

    def remove(self, key: int) -> None:
        h = hash(key)
        i = h % self.cap

        if self.map[i] is not None:
            for index in reversed(range(len(self.map[i]))):
                if self.map[i][index][0] == key:
                    return self.map[i].pop(index)
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)