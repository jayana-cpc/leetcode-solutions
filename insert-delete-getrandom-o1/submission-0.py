class RandomizedSet:

    def __init__(self):
        self.valList = []
        self.valDict = {}

    def insert(self, val: int) -> bool:
        if val not in self.valDict:
            self.valList.append(val)
            self.valDict[val] = len(self.valList) - 1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.valDict and len(self.valList) == 1:
            self.valList.pop()
            del self.valDict[val]
            return True

        elif val in self.valDict:
            self.valDict[self.valList[-1]] = self.valDict[val]
            self.valList[self.valDict[val]] = self.valList[-1]
            self.valList.pop()
            del self.valDict[val]
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.valList)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom() 