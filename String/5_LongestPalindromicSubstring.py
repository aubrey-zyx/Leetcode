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


class Solution2:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s

        max_len = 1
        start = 0
        dp = [[False] * n for _ in range(n)]  # dp[i][j] means whether s[i:j] is a palindrome
        for i in range(n):
            dp[i][i] = True

        for length in range(2, n + 1):
            for i in range(n):
                j = i + length - 1
                if j >= n:
                    break
                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    if length <= 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]

                if dp[i][j] and length > max_len:
                    max_len = length
                    start = i

        return s[start: start + max_len]