class RandomizedSet:

    def __init__(self):
        self.dict = {}
        self.lst = []

    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        self.dict[val] = len(self.lst)
        self.lst.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.dict:
            return False
        last, idx = self.lst[-1], self.dict[val]
        self.lst[idx], self.dict[last] = last, idx
        self.lst.pop()
        del self.dict[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.lst)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()