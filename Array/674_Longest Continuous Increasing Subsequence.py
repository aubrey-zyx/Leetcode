class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        l = r = 0
        for r in range(n):
            if r > 0 and nums[r - 1] >= nums[r]:
                l = r
            res = max(res, r - l + 1)
        return res