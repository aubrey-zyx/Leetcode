class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
        return dp[-1]


class Solution2:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        pre = cur = 0
        for i in range(2, n + 1):
            nxt = min(cur + cost[i - 1], pre + cost[i - 2])
            pre, cur = cur, nxt
        return cur


class Solution3:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * n
        dp[0], dp[1] = cost[0], cost[1]
        for i in range(2, n):
            dp[i] = min(dp[i - 2], dp[i - 1]) + cost[i]
        return min(dp[-2], dp[-1])