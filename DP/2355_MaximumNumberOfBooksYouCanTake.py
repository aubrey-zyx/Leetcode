class Solution:
    def maximumBooks(self, books: List[int]) -> int:
        n = len(books)
        dp = [0] * n
        stack = []
        for i in range(n):
            if books[i] == 0:
                stack.append(i)
                continue
            while stack:
                j = stack[-1]
                if books[j] >= books[i] - (i - j):
                    stack.pop()
                else:
                    break
            if not stack:
                j = -1
            start, end = books[i] - (i - j - 1), books[i]
            if start < 0:
                dp[i] = end * (end + 1) // 2
            else:
                dp[i] = (start + end) * (i - j) // 2
            if j >= 0:
                dp[i] += dp[j]
            stack.append(i)
        return max(dp)