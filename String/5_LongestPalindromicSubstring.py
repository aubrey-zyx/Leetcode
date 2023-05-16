class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s

        start, end = 0, 0
        for i in range(len(s)):
            len_odd = self.expandFromCenter(s, i, i)
            len_even = self.expandFromCenter(s, i, i + 1)
            length = max(len_odd, len_even)
            if length > end - start:
                start = i - (length - 1) // 2
                end = i + length // 2
        return s[start: end + 1]

    def expandFromCenter(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1