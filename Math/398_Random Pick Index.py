class Solution:

    def __init__(self, nums: List[int]):
        self.pos = defaultdict(list)
        for i, num in enumerate(nums):
            self.pos[num].append(i)

    def pick(self, target: int) -> int:
        return random.choice(self.pos[target])


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)


# Reservoir Sampling
# TLE
class Solution2:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        res = cnt = 0
        for i, num in enumerate(self.nums):
            if num == target:
                cnt += 1
                if random.randrange(cnt) == 0:
                    res = i
        return res