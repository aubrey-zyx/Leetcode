class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        res = []

        # diagnol heads are in the first row and the last column
        for d in range(m + n - 1):
            diagonal = []
            r = 0 if d < n else d - n + 1
            c = d if d < n else n - 1
            while r < m and c > -1:
                diagonal.append(mat[r][c])
                r += 1
                c -= 1
            if d % 2 == 0:
                res.extend(diagonal[::-1])
            else:
                res.extend(diagonal)

        return res


class Solution2:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []

        m, n = len(mat), len(mat[0])
        direction = 1
        res = []
        r = c = 0
        while r < m and c < n:
            res.append(mat[r][c])
            if direction == 1:
                nr, nc = r - 1, c + 1
            else:
                nr, nc = r + 1, c - 1

            # Find the next head if the next position is not within the bounds
            if nr < 0 or nr == m or nc < 0 or nc == n:
                if direction:
                    if c == n - 1:
                        r += 1
                    else:
                        c += 1
                else:
                    if r == m - 1:
                        c += 1
                    else:
                        r += 1
                direction = 1 - direction
            else:
                r, c = nr, nc

        return res