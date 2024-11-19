class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(len(prices) - 1):
            res += max(0, prices[i + 1] - prices[i])
        return res


class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        dp0 = 0  # No stock held
        dp1 = -prices[0]  # One stock held
        for i in range(1, len(prices)):
            new_dp0 = max(dp0, dp1 + prices[i])
            new_dp1 = max(dp0 - prices[i], dp1)
            dp0 = new_dp0
            dp1 = new_dp1
        return dp0