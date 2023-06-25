from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [1] * (rowIndex + 1)
        for i in range(2, rowIndex + 1):
            for j in range(i - 1, 0, -1):
                ans[j] += ans[j - 1]
        return ans


# binomial coefficient
class Solution2:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1] * (rowIndex + 1)
        for i in range(1, rowIndex):
            row[i] = row[i - 1] * (rowIndex - i + 1) // i
        return row