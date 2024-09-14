class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        x = sum(nums) % p
        if x == 0:
            return 0
        index = {0: -1}
        y = 0
        res = len(nums)
        for i, num in enumerate(nums):
            y = (y + num) % p
            if (y - x) % p in index:
                res = min(res, i - index[(y - x) % p])
            index[y] = i
        return res if res < len(nums) else -1