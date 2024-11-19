class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        res = 0
        nums_set = set(nums)
        for start in nums:
            cur = start
            streak = 0
            while cur in nums_set:
                streak += 1
                if cur * cur > 10 ** 5:
                    break
                cur *= cur
            res = max(res, streak)
        return res if res >= 2 else -1


class Solution2:
    def longestSquareStreak(self, nums: List[int]) -> int:
        lengths = {}
        nums.sort()
        for num in nums:
            root = int(num ** 0.5)
            if root * root == num and root in lengths:
                lengths[num] = lengths[root] + 1
            else:
                lengths[num] = 1
        res = max(lengths.values())
        return res if res > 1 else -1