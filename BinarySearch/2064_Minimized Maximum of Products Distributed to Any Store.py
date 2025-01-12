class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def is_possible(maximum):
            stores = 0
            for q in quantities:
                stores += math.ceil(q / maximum)
            return stores <= n

        lo, hi = max(sum(quantities) // n, 1), max(quantities)
        res = hi
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if is_possible(mid):
                res = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return res