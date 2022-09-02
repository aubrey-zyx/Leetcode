class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = ""
        while columnNumber:
            ans = chr(ord('A') + (columnNumber - 1) % 26) + ans
            columnNumber = (columnNumber - 1) // 26
        return ans