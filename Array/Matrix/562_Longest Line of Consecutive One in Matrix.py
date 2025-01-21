class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:
        row = defaultdict(int)
        col = defaultdict(int)
        diag = defaultdict(int)  # Descending diagonal
        anti_diag = defaultdict(int)  # Ascending diagonal

        res = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if not mat[i][j]:
                    row[i] = col[j] = diag[j - i] = anti_diag[j + i] = 0
                else:
                    row[i] += 1
                    col[j] += 1
                    diag[j - i] += 1
                    anti_diag[j + i] += 1
                    res = max(res, row[i], col[j], diag[j - i], anti_diag[j + i])
        return res