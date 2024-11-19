# Recursion with memorization
class Solution:
    def numDecodings(self, s: str) -> int:
        @lru_cache(maxsize=None)
        def dfs(s, i):
            if i == len(s):
                return 1
            if s[i] == "0":
                return 0
            if i == len(s) - 1:
                return 1
            res = dfs(s, i + 1)
            if int(s[i: i + 2]) <= 26:
                res += dfs(s, i + 2)
            return res

        return dfs(s, 0)


class Solution2:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 0 if s[0] == "0" else 1

        for i in range(1, n):
            if s[i] != "0":
                dp[i + 1] = dp[i]
            two_digit = int(s[i - 1: i + 1])
            if 10 <= two_digit <= 26:
                dp[i + 1] += dp[i - 1]

        return dp[-1]


class Solution3:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        first = second = 1
        for i in range(1, len(s)):
            cur = 0
            if s[i] != "0":
                cur = second
            two_digit = int(s[i - 1: i + 1])
            if 10 <= two_digit <= 26:
                cur += first
            first, second = second, cur
        return second