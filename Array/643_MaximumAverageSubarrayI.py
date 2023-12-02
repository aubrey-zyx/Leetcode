class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        res = cur_sum = sum(nums[:k])
        for r in range(k, len(nums)):
            cur_sum += nums[r]
            cur_sum -= nums[r - k]
            res = max(res, cur_sum)
        return res / k