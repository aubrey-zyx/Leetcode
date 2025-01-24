class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        rows, cols = len(points), len(points[0])
        prev = points[0]

        for r in range(1, rows):
            left_max = [0] * cols
            right_max = [0] * cols
            cur = [0] * cols

            left_max[0] = prev[0]
            for c in range(1, cols):
                left_max[c] = max(left_max[c - 1] - 1, prev[c])

            right_max[-1] = prev[-1]
            for c in range(cols - 2, -1, -1):
                right_max[c] = max(right_max[c + 1] - 1, prev[c])

            for c in range(cols):
                cur[c] = max(left_max[c], right_max[c]) + points[r][c]

            prev = cur

        return max(prev)


# Optimize to two pass for each row
class Solution2:
    def maxPoints(self, points: List[List[int]]) -> int:
        rows, cols = len(points), len(points[0])
        prev = points[0]

        for r in range(1, rows):
            running_max = 0
            for c in range(cols):
                running_max = max(running_max - 1, prev[c])
                prev[c] = running_max

            running_max = 0
            for c in range(cols - 1, -1, -1):
                running_max = max(running_max - 1, prev[c])
                prev[c] = max(prev[c], running_max) + points[r][c]

        return max(prev)