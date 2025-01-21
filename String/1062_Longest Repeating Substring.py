class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        n = len(s)
        suffixes = []
        for i in range(n):
            suffixes.append(s[i:])
        suffixes.sort()
        res = 0
        for i in range(1, n):
            j = 0
            while j < min(len(suffixes[i - 1]), len(suffixes[i])) and suffixes[i][j] == suffixes[i - 1][j]:
                j += 1
            res = max(res, j)
        return res


# Binary Search
class Solution2:
    def longestRepeatingSubstring(self, s: str) -> int:
        def has_repeating_substring(length):
            seen = set()
            for i in range(len(s) - length + 1):
                substring = s[i: i + length]
                if substring in seen:
                    return True
                seen.add(substring)
            return False

        l, r = 1, len(s) - 1
        res = 0
        while l <= r:
            m = (l + r) // 2
            if has_repeating_substring(m):
                res = l
                l = m + 1
            else:
                r = m - 1
        return res


# DP
class Solution3:
    def longestRepeatingSubstring(self, s: str) -> int:
        n = len(s)
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        res = 0
        for i in range(1, n + 1):
            for j in range(i + 1, n + 1):
                if s[i - 1] == s[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    res = max(res, dp[i][j])
        return res