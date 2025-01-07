class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_finish(m):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / m)
            return hours <= h

        l, r = 1, max(piles)
        res = r
        while l <= r:
            m = l + (r - l) // 2
            if can_finish(m):
                res = m
                r = m - 1
            else:
                l = m + 1
        return res