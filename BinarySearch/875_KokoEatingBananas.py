class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        while l <= r:
            k = (l + r) // 2
            time = 0
            for i in range(len(piles)):
                time += math.ceil(piles[i] / k)
            if time <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res