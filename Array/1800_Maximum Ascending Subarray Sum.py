class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        cur_sum = 0
        for i in range(n):
            if i == 0 or nums[i] > nums[i - 1]:
                cur_sum += nums[i]
            else:
                res = max(res, cur_sum)
                cur_sum = nums[i]
        res = max(res, cur_sum)
        return res