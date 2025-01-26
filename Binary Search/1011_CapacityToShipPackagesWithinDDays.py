class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def can_finish(capacity):
            days_needed = 1
            cur = 0
            for weight in weights:
                if cur + weight > capacity:
                    days_needed += 1
                    cur = 0
                cur += weight
            return days_needed <= days

        l, r = max(max(weights), math.ceil(sum(weights) / days)), sum(weights)
        while l < r:
            m = l + (r - l) // 2
            if can_finish(m):
                r = m
            else:
                l = m + 1
        return l