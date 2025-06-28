class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        res = 0
        for a in range(min(limit, n) + 1):
            if n - a > limit * 2:
                continue
            res += min(limit, n - a) - max(0, n - a - limit) + 1
        return res