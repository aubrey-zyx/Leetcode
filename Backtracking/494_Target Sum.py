# Recursion with Memorization / DP (Top-Down)
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def backtrack(i, cur_sum):
            if i == len(nums):
                return 1 if cur_sum == target else 0

            if (i, cur_sum) in memo:
                return memo[(i, cur_sum)]

            addition = backtrack(i + 1, cur_sum + nums[i])
            subtraction = backtrack(i + 1, cur_sum - nums[i])

            memo[(i, cur_sum)] = addition + subtraction

            return addition + subtraction

        return backtrack(0, 0)


# DP (Bottom-Up)
class Solution2:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n + 1)]
        dp[0][0] = 1

        for i in range(n):
            for total, count in dp[i].items():
                dp[i + 1][total + nums[i]] += count
                dp[i + 1][total - nums[i]] += count

        return dp[n][target]


# DP with optimized space
class Solution3:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)
        dp[0] = 1

        for num in nums:
            next_dp = defaultdict(int)
            for total, count in dp.items():
                next_dp[total + num] += count
                next_dp[total - num] += count
            dp = next_dp

        return dp[target]