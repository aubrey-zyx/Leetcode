class ProductOfNumbers:

    def __init__(self):
        self.pref_prod = [1]
        self.size = 0

    def add(self, num: int) -> None:
        if num == 0:
            self.pref_prod = [1]
            self.size = 0
        else:
            self.pref_prod.append(self.pref_prod[-1] * num)
            self.size += 1

    def getProduct(self, k: int) -> int:
        if k > self.size:
            return 0
        return self.pref_prod[-1] // self.pref_prod[self.size - k]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)