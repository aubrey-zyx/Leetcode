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