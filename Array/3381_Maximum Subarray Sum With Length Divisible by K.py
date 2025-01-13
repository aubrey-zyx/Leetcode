class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = float("-inf")
        pref_sum = 0
        min_pref_sum = [float("inf")] * k
        min_pref_sum[0] = 0
        for j in range(n):
            pref_sum += nums[j]
            remainder = (j + 1) % k
            res = max(res, pref_sum - min_pref_sum[remainder])
            min_pref_sum[remainder] = min(min_pref_sum[remainder], pref_sum)
        return res