class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        max_prod = min_prod = nums[0]
        res = max_prod
        for i in range(1, n):
            tmp_max = max(nums[i], max_prod * nums[i], min_prod * nums[i])
            min_prod = min(nums[i], max_prod * nums[i], min_prod * nums[i])
            max_prod = tmp_max
            res = max(res, max_prod)
        return res