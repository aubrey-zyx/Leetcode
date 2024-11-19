class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        l = 0
        last_zero = -1
        for r in range(n):
            if nums[r] == 0:
                l = last_zero + 1
                last_zero = r
            res = max(res, r - l)
        return res