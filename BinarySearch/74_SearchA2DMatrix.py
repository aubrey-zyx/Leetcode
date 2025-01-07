class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m * n - 1
        while l <= r:
            mid = l + (r - l) // 2
            mid_num = matrix[mid // n][mid % n]
            if target < mid_num:
                r = mid - 1
            elif target > mid_num:
                l = mid + 1
            else:
                return True
        return False


class Solutio2:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        t, b = 0, m - 1  # top & bottom
        while t <= b:
            row = t + (b - t) // 2
            if target < matrix[row][0]:
                b = row - 1
            elif target > matrix[row][-1]:
                t = row + 1
            else:
                break

        if t > b:
            return False

        row = t + (b - t) // 2
        l, r = 0, n - 1
        while l <= r:
            m = l + (r - l) // 2
            if target < matrix[row][m]:
                r = m - 1
            elif target > matrix[row][m]:
                l = m + 1
            else:
                return True
        return False