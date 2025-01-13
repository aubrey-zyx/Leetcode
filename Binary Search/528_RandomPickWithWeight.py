class Solution:

    def __init__(self, w: List[int]):
        self.pref_sum = []
        cur_sum = 0
        for weight in w:
            cur_sum += weight
            self.pref_sum.append(cur_sum)
        self.total = cur_sum

    def pickIndex(self) -> int:
        random_num = random.randint(1, self.total)
        return bisect_left(self.pref_sum, random_num)


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()