class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1, n2 = len(word1), len(word2)
        if n1 == 0:
            return n2
        if n2 == 0:
            return n1
        dp = [[0 for _ in range(n2 + 1)] for _ in range(n1 + 1)]
        for i1 in range(1, n1 + 1):
            dp[i1][0] = i1
        for i2 in range(1, n2 + 1):
            dp[0][i2] = i2
        for i1 in range(1, n1 + 1):
            for i2 in range(1, n2 + 1):
                if word2[i2 - 1] == word1[i1 - 1]:
                    dp[i1][i2] = dp[i1 - 1][i2 - 1]
                else:
                    insert = dp[i1][i2 - 1]
                    delete = dp[i1 - 1][i2]
                    replace = dp[i1 - 1][i2 - 1]
                    dp[i1][i2] = min(insert, delete, replace) + 1
        return dp[-1][-1]