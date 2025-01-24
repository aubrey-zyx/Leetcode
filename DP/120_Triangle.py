class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        prev = triangle[0]
        for r in range(1, len(triangle)):
            cur = []
            for c in range(r + 1):
                smallest_above = math.inf
                if c > 0:
                    smallest_above = prev[c - 1]
                if c < r:
                    smallest_above = min(smallest_above, prev[c])
                cur.append(triangle[r][c] + smallest_above)
            prev = cur
        return min(prev)


# In-place
class Solution2:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for r in range(1, len(triangle)):
            for c in range(r + 1):
                smallest_above = math.inf
                if c > 0:
                    smallest_above = triangle[r - 1][c - 1]
                if c < r:
                    smallest_above = min(smallest_above, triangle[r - 1][c])
                triangle[r][c] += smallest_above
        return min(triangle[-1])