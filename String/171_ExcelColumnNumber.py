class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        for x in columnTitle:
            ans *= 26
            ans += ord(x) - ord('A') + 1
        return ans