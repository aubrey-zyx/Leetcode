class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        groups = {}
        rows, cols = len(matrix), len(matrix[0])
        for r in range(rows):
            for c in range(cols):
                if r - c not in groups:
                    groups[r - c] = matrix[r][c]
                elif groups[r - c] != matrix[r][c]:
                    return False
        return True

    
class Solution2:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        for r in range(rows):
            for c in range(cols):
                if r != 0 and c != 0 and matrix[r][c] != matrix[r - 1][c - 1]:
                    return False
        return True