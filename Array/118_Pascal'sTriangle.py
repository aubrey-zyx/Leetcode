from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[1]]
        for i in range(1, numRows):
            new = [1] * (i + 1)
            for j in range(1, i):
                new[j] = triangle[i-1][j-1] + triangle[i-1][j]
            triangle.append(new)
        return triangle