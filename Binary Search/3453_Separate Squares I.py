class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        M = 100_000
        area_total = sum(l * l for _, _, l in squares)

        def check(y):
            area_below = 0
            for _, yi, l in squares:
                if yi < y:
                    area_below += l * min(y - yi, l)
            return area_below >= area_total / 2

        left = 0
        max_y = right = max(y + l for _, y, l in squares)
        for _ in range((max_y * M).bit_length()):
            mid = (left + right) / 2
            if check(mid):
                right = mid
            else:
                left = mid
        return (left + right) / 2


class Solution2:
    def separateSquares(self, squares: List[List[int]]) -> float:
        M = 100_000
        squares = [[M * x, M * y, M * l] for x, y, l in squares]
        area_total = sum(l * l for _, _, l in squares)

        def check(y):
            area_below = 0
            for _, yi, l in squares:
                if yi < y:
                    area_below += l * min(y - yi, l)
            return 2 * area_below >= area_total

        l = min(y for _, y, _ in squares)
        r = max(y + l for _, y, l in squares)
        while l < r:
            mid = (l + r) // 2
            if check(mid):
                r = mid
            else:
                l = mid + 1
        return l / M