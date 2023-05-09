class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        for x in columnTitle:
            ans *= 26
            ans += ord(x) - ord('A') + 1
        return ans


'''
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        num = 0
        pos = 0
        for letter in reversed(columnTitle):
            num += (ord(letter) - ord("A") + 1) * 26 ** pos
            pos += 1
        return num
'''