class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        res = 0
        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    res = max(res, i - stack[-1])
        return res


# DP
class Solution2:
    def longestValidParentheses(self, s: str) -> int:
        res = 0
        n = len(s)
        dp = [0] * n
        for i in range(1, n):
            if s[i] == ")":
                if s[i - 1] == "(":
                    dp[i] = (dp[i - 2] if i >= 2 else 0) + 2
                elif i - dp[i - 1] > 0 and s[i - dp[i - 1] - 1] == "(":
                    dp[i] = (
                        dp[i - 1]
                        + (dp[i - dp[i - 1] - 2] if i - dp[i - 1] >= 2 else 0)
                        + 2
                    )
                res = max(res, dp[i])
        return res


# Two counters. O(1) space
class Solution3:
    def longestValidParentheses(self, s: str) -> int:
        l = r = res = 0
        for i in range(len(s)):
            if s[i] == "(":
                l += 1
            else:
                r += 1
            if l == r:
                res = max(res, 2 * r)
            elif r > l:
                l = r = 0
        l = r = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "(":
                l += 1
            else:
                r += 1
            if l == r:
                res = max(res, 2 * l)
            elif l > r:
                l = r = 0
        return res