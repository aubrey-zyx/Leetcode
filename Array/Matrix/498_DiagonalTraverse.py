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